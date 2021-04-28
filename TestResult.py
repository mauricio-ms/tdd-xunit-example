class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
        self.logExceptions = ""

    def testStarted(self):
        self.runCount = self.runCount + 1

    def testFailed(self, testCase, e):
        self.errorCount = self.errorCount + 1
        self.logExceptions = self.logExceptions + \
            ", %s.%s-%s" % (testCase.__class__.__name__, testCase.name, e.__class__.__name__)

    def summary(self):
        return "%d run, %d failed%s" % (self.runCount, self.errorCount, self.logExceptions)
