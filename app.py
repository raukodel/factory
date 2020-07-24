from core import Core
from database import Database
from webserver import Webserver
from exceptionHandler import ExceptionHandler
from saveStackTraceLog import SaveStackTraceLog

try:
    classes = {
       "database" : Database(), 
        "webserver" : Webserver(), 
        "exceptionHandler" : ExceptionHandler(SaveStackTraceLog()),
        "saveLog" : SaveStackTraceLog()
    }

    core = Core(classes)
    core.start()
    core.stop()
except Exception as e:
    exceptionHandler = ExceptionHandler(SaveStackTraceLog())
    exceptionHandler.handleException(e)
finally:
    print("Terminated")