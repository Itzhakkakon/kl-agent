from interfaces.i_encryptor import IEncryptor

class XOREncryptor(IEncryptor):
    def __init__(self, key: bytes):
        self.key = key

    def encrypt(self, data: bytes) -> bytes:
        result = bytearray()
        for i in range(len(data)):
            result.append(data[i] ^ self.key[i % len(self.key)])
        return bytes(result)

    def decrypt(self, data: bytes) -> bytes:
        # XOR is symmetric, so decrypt is the same as encrypt
        return self.encrypt(data)

