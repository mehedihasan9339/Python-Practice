class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.isOpen = False


    def open(self):
        if self.isOpen:
            raise InvalidOperationError("Stream is already opened!")
        self.isOpen = True


    def close(self):
        if not self.isOpen:
            raise InvalidOperationError("Stream is already closed!")
        self.isOpen = False


class FileStream(Stream):
    def read(self):
        if not self.isOpen:
            raise InvalidOperationError("Stream is not opened yet!")
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        if not self.isOpen:
            raise InvalidOperationError("Stream is not opened yet!")
        print("Reading data from a network")


fs = FileStream()
fs.open()
fs.read() # Reading data from a file
# fs.open() # InvalidOperationError: Stream is already opened!
fs.close()
