from implementations.writers.file_writer import FileWriter
from implementations.writers.network_writer import NetworkWriter
from interfaces.i_writer import IWriter

class WriterFactory:
    """Available writer types: file, network"""
    @staticmethod
    def create_writer(writer_type: str, destination: str) -> IWriter:
        if writer_type == "file":
            return FileWriter(destination)
        elif writer_type == "network":
            return NetworkWriter(destination)
        raise ValueError(f"Unknown writer type: {writer_type}")