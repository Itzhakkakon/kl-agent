from interfaces.i_writer import IWriter

class FileWriter(IWriter):
    """File implementation of writer interface"""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file = open(file_path, "w", encoding='utf-8')
        
    def write(self, data: str):
        """Write data to the file"""
        self.file.write(data)
        self.file.flush()  # Ensure data is written immediately
        
    def close(self):
        """Close the file"""
        if self.file and not self.file.closed:
            self.file.close()