from agent.interfaces.i_encryptor import IEncryptor

class XOREncryptor(IEncryptor):
    def __init__(self, key: bytes):
        self.key = key

    # TODO: Implement the XOR encryption algorithm
    def encrypt(self, data: bytes) -> bytes:
        ...
        
