import re

def clean_window_title(window_title: str) -> str:
    """
    Clean the window title by removing bidirectional control characters
    and normalizing whitespace.
    
    Args:
        window_title: The raw window title to clean
        
    Returns:
        A cleaned window title string
    """
    if not window_title:
        return ""
    
    # Remove bidirectional control characters
    bidi_controls = ['\u202A', '\u202B', '\u202C', '\u202D', '\u202E',
                     '\u200E', '\u200F', '\u061C']
    
    clean_title = window_title
    for char in bidi_controls:
        clean_title = clean_title.replace(char, '')
    
    # Normalize whitespace
    clean_title = ' '.join(clean_title.split())
    
    return clean_title
