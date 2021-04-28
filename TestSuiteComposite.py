from TestSuite import TestSuite


class TestSuiteComposite(TestSuite):
    def add(self, testCase):
        test_names = [method_name for method_name in dir(testCase)
                      if method_name.startswith("test") and callable(getattr(testCase, method_name))]
        for test_name in test_names:
            super().add(testCase.__class__(test_name))
