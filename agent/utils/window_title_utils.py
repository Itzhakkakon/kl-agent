import re

class WindowTitleUtils:
    @staticmethod
    def clean_window_title(window_title: str) -> str:
        """Clean the window title by removing sensitive or strange unreadable characters."""
        if not window_title:
            return "Unknown"
        
        # Remove trailing and leading whitespace
        cleaned_title = window_title.strip()
        
        # Filter out strange characters like right-to-left marks and other special Unicode characters
        # \u200f is RIGHT-TO-LEFT MARK, \u200e is LEFT-TO-RIGHT MARK
        special_chars = ['\u200f', '\u200e', '\u202e', '\u202b', '\ufeff', '‏', '‎']
        for char in special_chars:
            cleaned_title = cleaned_title.replace(char, '')
            
        # Use regex to remove other control characters
        cleaned_title = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_title)
        
        return cleaned_title
