from interfaces.i_window_title import IWindowTitle
from .linux.window_title_methods import LinuxWindowTitleMethods

class LinuxWindowTitle(IWindowTitle):
    def get_active_window_title(self) -> str:
        methods = LinuxWindowTitleMethods()
        
        # Try different methods in order of preference
        for method_name in ["try_xdotool", "try_ewmh", "try_xprop", "try_wmctrl", "try_xlib"]:
            try:
                method = getattr(methods, method_name)
                title = method()
                if title and title not in ["Unknown", "No window found", "Error"]:
                    return title
            except Exception:
                continue
        
        return "Unknown"
