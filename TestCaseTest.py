from SetUpError import SetUpError
from TearDownError import TearDownError
from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testSetUpFailedResult(self):
        test = SetUpError("testMethod")
        test.run(self.result)
        assert "1 run, 1 failed, SetUpError.testMethod-Exception" == self.result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert "1 run, 1 failed, WasRun.testBrokenMethod-Exception" == self.result.summary()

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed(WasRun("testMethod"), Exception())
        assert "1 run, 1 failed, WasRun.testMethod-Exception" == self.result.summary()

    def testTearDownFailedResult(self):
        test = TearDownError("testMethod")
        test.run(self.result)
        assert "1 run, 1 failed, TearDownError.testMethod-Exception" == self.result.summary()

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert "2 run, 1 failed, WasRun.testBrokenMethod-Exception" == self.result.summary()

    def testSetUpErrorsReport(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(SetUpError("testMethod", ZeroDivisionError))
        suite.add(SetUpError("testBrokenMethod", ValueError))
        suite.run(self.result)
        assert "3 run, 2 failed, SetUpError.testMethod-ZeroDivisionError, SetUpError.testBrokenMethod-ValueError" == \
               self.result.summary()


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testSetUpFailedResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testTearDownFailedResult"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("testSetUpErrorsReport"))

result = TestResult()
suite.run(result)
print(result.summary())
