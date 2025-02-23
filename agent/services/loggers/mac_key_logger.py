from interfaces.i_key_logger import IKeyLogger

#TODO: Implement MacKeyLogger
class MacKeyLogger(IKeyLogger):
    def __init__(self):
        self.logged_keys = []
    
    def start(self):
        # macOS-specific implementation using AppKit
        pass

    def stop(self):
        pass

    def get_pressed_keys(self):
        return self.logged_keys