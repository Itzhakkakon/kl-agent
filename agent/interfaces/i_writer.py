from abc import ABC, abstractmethod
from models.keystroke import Keystroke

class IWriter(ABC):
    @abstractmethod
    def write(self, keystroke: Keystroke) -> None:
        """Write a keystroke."""
        pass
    
    @abstractmethod
    def flush(self) -> None:
        """Flush pending data to storage."""
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Close the writer and clean up resources."""
        pass
