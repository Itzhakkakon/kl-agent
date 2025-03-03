from pynput.keyboard import Key, KeyCode
from utils.window_title_utils import clean_window_title

class Keystroke:
    def __init__(self, key: Key, timestamp: float, window: str = ""):
        self.key = key
        self.timestamp = timestamp
        self.window = window
    
    def __str__(self) -> str:
        """Return string representation of the key.""" 
               
        if isinstance(self.key, Key):
            return f"[{self.key.name}]"
        elif isinstance(self.key, KeyCode):
            if self.key.char is None:
                return f"[{self.key.vk}]"
            return self.key.char
        
    def __repr__(self) -> str:
        """Return the representation of the keystroke."""
        return f"Keystroke(key={self.key}, timestamp={self.timestamp}, window='{self.window}')"
    
    def to_dict(self) -> dict:
        """Return dictionary representation of the keystroke."""
        return {
            "key": str(self),
            "timestamp": self.timestamp,
            "window": clean_window_title(self.window)
        }
    
    # @staticmethod
    # def json_serialize(obj):
    #     """Custom JSON serializer for Keystroke objects."""
    #     if isinstance(obj, Keystroke):
    #         return obj.to_dict()
    #     raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")