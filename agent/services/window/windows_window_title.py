from interfaces.i_window_title import IWindowTitle
import win32gui # pip install pywin32

class WindowsWindowTitle(IWindowTitle):
    def get_active_window_title(self) -> str:
        try:
            window = win32gui.GetForegroundWindow()
            return win32gui.GetWindowText(window)
        except Exception:
            return ""