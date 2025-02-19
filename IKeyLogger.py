from abc import ABC, abstractmethod
from typing import List

class IKeyLogger(ABC):
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
