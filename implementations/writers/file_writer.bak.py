from typing import List
import time

class FileWriter:
    def __init__(self, filename="log.txt"):
        self.filename = filename

    def write_to_file(self, data: List[str]):
        """כותב את הנתונים לקובץ עם חותמת זמן"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] " + " ".join(data) + "\n")

