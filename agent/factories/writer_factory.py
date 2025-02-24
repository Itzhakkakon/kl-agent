from interfaces.i_writer import IWriter

class WriterFactory:
    @staticmethod
    def create_writer(writer_type: str, destination: str) -> IWriter:
        if writer_type == "file":
            from services.writers.file_writer import FileWriter
            return FileWriter(destination)
        elif writer_type == "network":
            from services.writers.network_writer import NetworkWriter
            return NetworkWriter(destination)
        
        raise ValueError(f"Unknown writer type: {writer_type}")
