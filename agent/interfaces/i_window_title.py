from abc import ABC, abstractmethod

class IWindowTitle(ABC):
    @abstractmethod
    def get_active_window_title(self) -> str:
        pass
