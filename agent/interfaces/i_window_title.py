from abc import ABC, abstractmethod

class IWindowTitle(ABC):
    """Interface for window title tracking functionality"""
    
    @abstractmethod
    def get_active_window_title(self) -> str:
        """Get the title of the currently active window"""
        pass
