from WasRun import WasRun


class TearDownError(WasRun):
    def tearDown(self):
        raise Exception()
