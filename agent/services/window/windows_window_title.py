from interfaces.i_window_title import IWindowTitle

class WindowsWindowTitle(IWindowTitle):
    def get_active_window_title(self) -> str:
        ...