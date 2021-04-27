from TestCase import TestCase


class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1
