import time
import json
from pynput.keyboard import Key

class Keystroke:
    def __init__(self, key: Key, timestamp: float, window: str = ""):
        self.key = key
        self.timestamp = timestamp
        self.window = window
    
    def __str__(self) -> str:
        """Return string representation of the key."""
        if self.key == Key.space: return " "
        if self.key == Key.enter: return "\n"
        if self.key == Key.tab: return "\t"
        
        try:
            return self.key.char
        except AttributeError:
            return str(self.key)
        except:
            return ""
    
    def __repr__(self) -> str:
        """Return the representation of the keystroke."""
        return f"Keystroke(key={self.key}, timestamp={self.timestamp}, window='{self.window}')"
    
    def to_dict(self) -> dict:
        """Return dictionary representation of the keystroke."""
        return {
            "key": str(self),
            "timestamp": self.timestamp,
            "window": self.window
        }