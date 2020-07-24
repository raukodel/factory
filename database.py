class IDataBase:

    def __init__(self):
        pass

    def start(self):
        raise NotImplementedError("Database start not implemented")

    def stop(self):
        raise NotImplementedError("Database stop not implemented")

class Database(IDataBase):
    
    def __init__(self):
        super().__init__()

    def start(self):
        print("[Database] >>> Started")

    def stop(self):
        print("[Database] >>> Stopped")