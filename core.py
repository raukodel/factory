class Core():

    def __init__(self, classes):
        super().__init__()

        self.database = classes["database"]
        self.webserver = classes["webserver"]
        self.exceptionHandler = classes["exceptionHandler"]

    def start(self):
        print("[Core] >>> Starting")
        
        try:
            self.database.start()
            self.webserver.start()
        except (Exception, NotImplementedError) as e:
            self.exceptionHandler.handleException(e)

        print("[Core] >>> Started")

    def stop(self):
        print("[Core] >>> Stopping")

        try:
            self.database.stop()
            self.webserver.stop()
        except (Exception, NotImplementedError) as e:
            self.exceptionHandler.handleException(e)

        print("[Core] >>> Stopped")