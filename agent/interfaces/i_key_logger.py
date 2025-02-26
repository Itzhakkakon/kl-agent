from abc import ABC, abstractmethod
from typing import List
from interfaces.i_writer import IWriter

class IKeyLogger(ABC):
    """Interface for key logging functionality"""
    
    @abstractmethod
    def __init__(self, writer: IWriter):
        pass
    
    @abstractmethod
    def start(self):
        """Start the key logger"""
        pass

    @abstractmethod
    def stop(self):
        """Stop the key logger"""
        pass

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        """Return the list of collected keystrokes"""
        pass
