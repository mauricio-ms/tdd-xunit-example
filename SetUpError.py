from WasRun import WasRun


class SetUpError(WasRun):
    def __init__(self, name, e=Exception()):
        self._e = e
        WasRun.__init__(self, name)

    def setUp(self):
        raise self._e
