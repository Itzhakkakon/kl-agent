import time
from typing import Optional
from interfaces.i_key_logger import IKeyLogger
from interfaces.i_writer import IWriter
from factories.window_title_factory import WindowTitleFactory
from models.keystroke import Keystroke

class BaseKeyLogger(IKeyLogger):
    def __init__(self, writer: IWriter):
        self.writer = writer
        self.running = False
        self.window_title_getter = WindowTitleFactory.create_window_title()
    
    def start(self) -> None:
        """Start the key logger."""
        self.running = True
        self._start_listening()
    
    def stop(self) -> None:
        """Stop the key logger."""
        self.running = False
        self._stop_listening()
    
    def _create_keystroke(self, key) -> Keystroke:
        """Create a keystroke object from the key."""
        timestamp = time.time()
        window_title = self.window_title_getter.get_active_window_title()
        return Keystroke(key, timestamp, window_title)
    
    def _process_key(self, key) -> None:
        """Process a key press event."""
        keystroke = self._create_keystroke(key)
        self.writer.write(keystroke)
    
    def _start_listening(self) -> None:
        """Platform-specific implementation to start listening for keystrokes."""
        raise NotImplementedError("Subclasses must implement this method")
    
    def _stop_listening(self) -> None:
        """Platform-specific implementation to stop listening for keystrokes."""
        raise NotImplementedError("Subclasses must implement this method")
