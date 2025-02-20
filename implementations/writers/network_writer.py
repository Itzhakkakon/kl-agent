from interfaces.i_writer import IWriter
import requests

class NetworkWriter(IWriter):
    def __init__(self, url: str):
        self.url = url

    def write(self, data: str) -> None:
        requests.post(self.url, json={'data': data})

    def close(self) -> None:
        pass