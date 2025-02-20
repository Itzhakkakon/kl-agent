from interfaces.i_key_logger import IKeyLogger

#TODO: Implement LinuxKeyLogger
class LinuxKeyLogger(IKeyLogger):
    def __init__(self):
        self.logged_keys = []
    
    def start_logging(self):
        # Linux-specific implementation using evdev
        pass

    def stop_logging(self):
        pass

    def get_pressed_keys(self):
        return self.logged_keys