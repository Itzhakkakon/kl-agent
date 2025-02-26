from abc import ABC, abstractmethod

class IWriter(ABC):
    """Interface for writing data"""
    
    @abstractmethod
    def write(self, data: str):
        """Write data to the destination"""
        pass
    
    @abstractmethod
    def close(self):
        """Close any open resources"""
        pass
