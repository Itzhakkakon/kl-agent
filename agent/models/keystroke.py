import time
from typing import Any, Union
from pynput.keyboard import Key

class Keystroke:
    NON_PRINTABLE_KEYS = (
        Key.alt, Key.alt_gr, Key.alt_l, Key.alt_r,
        Key.backspace, Key.caps_lock,
        Key.cmd, Key.cmd_l, Key.cmd_r,
        Key.ctrl, Key.ctrl_l, Key.ctrl_r,
        Key.delete, Key.down, Key.end, Key.enter, Key.esc,
        Key.f1, Key.f2, Key.f3, Key.f4, Key.f5, Key.f6,
        Key.f7, Key.f8, Key.f9, Key.f10, Key.f11, Key.f12,
        Key.home, Key.insert, Key.left,
        Key.media_next, Key.media_play_pause, Key.media_previous,
        Key.media_volume_down, Key.media_volume_mute, Key.media_volume_up,
        Key.menu, Key.num_lock,
        Key.page_down, Key.page_up, Key.pause, Key.print_screen,
        Key.right, Key.scroll_lock,
        Key.shift, Key.shift_l, Key.shift_r,
        Key.space, Key.tab, Key.up,
    )
    
    def __init__(self, key: Any, timestamp: float, window: str = ""):
        self.key = key
        self.timestamp = timestamp
        self.window = window
    
    def get_struct_time(self):
        """Return the structured time tuple for the timestamp."""
        return time.gmtime(self.timestamp)
    
    def are_keystrokes_within_same_second(self, other: 'Keystroke') -> bool:
        """Check if two keystrokes occurred in the same second."""
        # struct_time[:6] returns tuple(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec)
        return self.get_struct_time()[:6] == other.get_struct_time()[:6]
    
    def __str__(self) -> str:
        """Return string representation of the key."""
        if isinstance(self.key, Key):
            # Handle special keys
            return f"{self.key.name}"
        # Handle regular characters
        return f"{self.key}"
    
    def __repr__(self) -> str:
        """Return the representation of the keystroke."""
        return f"Keystroke(key={self.key}, timestamp={self.timestamp}, window='{self.window}')"
    
    def to_dict(self) -> dict:
        """Convert keystroke to dictionary for JSON serialization."""
        return {
            "key": str(self),
            "timestamp": self.timestamp,
            "window": self.window
        }
