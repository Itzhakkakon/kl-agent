from abc import ABC, abstractmethod

class IEncryptor(ABC):
    @abstractmethod
    def encrypt(self, data: bytes) -> bytes:
        pass
