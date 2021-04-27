from WasRun import WasRun


class SetUpError(WasRun):
    def setUp(self):
        raise Exception
