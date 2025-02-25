import os
import json
import time
from typing import List, Dict, Any
from interfaces.i_writer import IWriter
from models.keystroke import Keystroke

class JsonWriter(IWriter):
    def __init__(self, base_dir: str = "keystrokes"):
        """
        Initialize JSON writer with a base directory.
        
        Args:
            base_dir: Base directory for storing keystroke files
        """
        self.base_dir = base_dir
        self.current_keystrokes = []
        self.last_flush_timestamp = 0
        # Ensure base directory exists
        os.makedirs(self.base_dir, exist_ok=True)
    
    def _get_day_timestamp(self, timestamp: float) -> int:
        """Get timestamp for the start of the day (UTC midnight)."""
        struct_time = time.gmtime(timestamp)
        # Create a timestamp for midnight (00:00:00) of the same day
        day_start = time.mktime((
            struct_time.tm_year,
            struct_time.tm_mon,
            struct_time.tm_mday,
            0,  # hour
            0,  # minute
            0,  # second
            struct_time.tm_wday,
            struct_time.tm_yday,
            struct_time.tm_isdst
        ))
        return int(day_start)
    
    def _get_hour(self, timestamp: float) -> int:
        """Get hour from timestamp."""
        return time.gmtime(timestamp).tm_hour
    
    def _get_file_path(self, keystroke: Keystroke) -> str:
        """
        Get the file path for a keystroke based on its timestamp.
        
        Format: {base_dir}/{day_timestamp}/{hour}.json
        """
        day_timestamp = self._get_day_timestamp(keystroke.timestamp)
        hour = self._get_hour(keystroke.timestamp)
        
        day_dir = os.path.join(self.base_dir, str(day_timestamp))
        os.makedirs(day_dir, exist_ok=True)
        
        return os.path.join(day_dir, f"{hour}.json")
    
    def write(self, keystroke: Keystroke) -> None:
        """Add a keystroke to the current batch."""
        self.current_keystrokes.append(keystroke)
        # Flush every 10 keystrokes or if last flush was more than 5 seconds ago
        current_time = time.time()
        if len(self.current_keystrokes) >= 10 or (current_time - self.last_flush_timestamp) > 5:
            self.flush()
    
    def flush(self) -> None:
        """Write all pending keystrokes to their appropriate files."""
        if not self.current_keystrokes:
            return
            
        # Group keystrokes by file path
        keystrokes_by_file: Dict[str, List[Dict[str, Any]]] = {}
        for ks in self.current_keystrokes:
            file_path = self._get_file_path(ks)
            if file_path not in keystrokes_by_file:
                keystrokes_by_file[file_path] = []
            keystrokes_by_file[file_path].append(ks.to_dict())
        
        # Write each group to its file
        for file_path, keystrokes in keystrokes_by_file.items():
            # Load existing keystrokes if file exists
            existing_keystrokes = []
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r') as f:
                        existing_keystrokes = json.load(f)
                except json.JSONDecodeError:
                    # File might be empty or corrupted, start fresh
                    existing_keystrokes = []
            
            # Append new keystrokes
            all_keystrokes = existing_keystrokes + keystrokes
            
            # Write back to file
            with open(file_path, 'w') as f:
                json.dump(all_keystrokes, f, indent=2)
        
        # Clear the current batch and update last flush time
        self.current_keystrokes = []
        self.last_flush_timestamp = time.time()
    
    def close(self) -> None:
        """Ensure all keystrokes are written before closing."""
        self.flush()
