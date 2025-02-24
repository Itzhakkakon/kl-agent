from interfaces.i_encryptor import IEncryptor

class DummyEncryptor(IEncryptor):
    def encrypt(self, data: bytes) -> bytes:
        return data
