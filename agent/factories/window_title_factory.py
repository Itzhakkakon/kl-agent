from interfaces.i_window_title import IWindowTitle
from utils.system_info import get_system_name

class WindowTitleFactory:
    @staticmethod
    def create_window_title() -> IWindowTitle:
        system = get_system_name()
        
        if system == "windows":
            from services.window.windows_window_title import WindowsWindowTitle
            return WindowsWindowTitle()
        elif system == "linux":
            from services.window.linux_window_title import LinuxWindowTitle
            return LinuxWindowTitle()
        elif system == "darwin": # macOS
            from services.window.mac_window_title import MacWindowTitle
            return MacWindowTitle()
        
        raise NotImplementedError(f"No window title implementation for {system}")
