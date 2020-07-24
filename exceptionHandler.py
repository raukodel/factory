import traceback

class IExceptionHandler:

    def __init__(self):
        pass

    def handleException(self, e):
        raise NotImplementedError("ExceptionHandler handleException not implemented")

class ExceptionHandler(IExceptionHandler):

    def __init__(self, saveLog):
        super().__init__()

        self.saveStackTraceLog = saveLog

    def handleException(self, e):
        try:
            tracebackInfo = traceback.format_exc()
            self.saveStackTraceLog.saveLog(tracebackInfo)
        except Exception as e:
            pass