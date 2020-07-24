import re
from datetime import datetime

class ISaveLog:

    def __init__(self):
        pass

    def __createLogFile(self):
        raise NotImplementedError("SaveLog __createLogFile not implemented")

    def __formatInformation(self, information):
        raise NotImplementedError("SaveLog __formatInformation not implemented")
 
    def __writeLogFile(self, information):
        raise NotImplementedError("SaveLog __writeLogFile not implemented")

    def saveLog(self, information):
        raise NotImplementedError("SaveLog saveLog not implemented")

class SaveStackTraceLog(ISaveLog):

    def __init__(self):
        super().__init__()

    def __createLogFile(self):
        dateTimeNow = datetime.now()
        fileToSave = open("log_" + dateTimeNow.strftime("%d-%m-%Y") + ".txt","a+")
        fileToSave.write("----------" + dateTimeNow.strftime("%d/%m/%Y. %H:%M:%S"))
        return fileToSave

    def __formatStackTrace(self, information):
        return {
            "classNames" : re.findall("\\w+.py", information),
            "classLines" : re.findall("\s*\d+\s*", information),
            "methodCall" : re.findall("    .*", information)
        }

    def __writeLogFile(self, information, fileToSave):
        formatedStackTrace = ""

        for idx, names in enumerate(information["classNames"]):
            className = re.sub("\s", "", information["classNames"][idx])
            classLine = re.sub("\s", "", information["classLines"][idx])
            methodCall = information["methodCall"][idx]
            methodCallNoInitialWhiteSpace = methodCall[len(methodCall) - len(methodCall.lstrip()):]
            
            formatedStackTrace = "\n    " + ("-" * idx) + "> " + className + " " + classLine + " " + methodCallNoInitialWhiteSpace
            fileToSave.write(formatedStackTrace)

        fileToSave.write("\n\n")

    def saveLog(self, information):
        try:
            fileToSave = self.__createLogFile()
            formatedInformation = self.__formatStackTrace(information)        
            self.__writeLogFile(formatedInformation, fileToSave)
        except Exception as e:
            pass
        
        