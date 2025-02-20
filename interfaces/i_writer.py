from abc import ABC, abstractmethod
from typing import Any

class IWriter(ABC):
    @abstractmethod
    def write(self, data: Any):
        pass

    @abstractmethod
    def close(self):
        pass
    