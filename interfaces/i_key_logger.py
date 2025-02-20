from abc import ABC, abstractmethod
from typing import List
from interfaces.i_writer import IWriter

class IKeyLogger(ABC):
    @abstractmethod
    def __init__(self, writer: IWriter):
        pass
    
    @abstractmethod
    def start_logging(self) -> None:
        """Start listening to keyboard events"""
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        """Stop listening to keyboard events"""
        pass

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        """Return the list of collected keystrokes"""
        pass
