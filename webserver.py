class IWebserver:

    def __init__(self):
        pass

    def start(self):
        raise NotImplementedError("Webserver start not implemented")

    def stop(self):
        raise NotImplementedError("Webserver stop not implemented")

class Webserver(IWebserver):

    def __init__(self):
        super().__init__()

    def start(self):
        print("[Webserver] >>> Started")

    def stop(self):
        print("[Webserver] >>> Stopped")