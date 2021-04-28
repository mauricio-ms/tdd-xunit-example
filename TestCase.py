class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self, result):
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
            self.tearDown()
        except Exception as e:
            result.testFailed(self, e)

    def tearDown(self):
        pass
