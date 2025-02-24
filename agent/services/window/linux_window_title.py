from interfaces.i_window_title import IWindowTitle
from .linux.window_title_methods import LinuxWindowTitleMethods

class LinuxWindowTitle(IWindowTitle):
    @staticmethod
    def get_active_window_title() -> str:
        methods = LinuxWindowTitleMethods()
        try:
            title = methods.try_xdotool()
            if title and title not in ["Unknown", "No window found", "Error"]:
                # print(f"Window title: {title}", "from try_xdotool")
                return title
        except:
            pass
        return "Unknown"
