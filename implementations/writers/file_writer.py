from interfaces.i_writer import IWriter

class FileWriter(IWriter):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.file = None

    def write(self, data: str) -> None:
        if not self.file:
            self.file = open(self.filepath, 'a')
        self.file.write(data + '\n')
        self.file.flush()

    def close(self) -> None:
        if self.file:
            self.file.close()