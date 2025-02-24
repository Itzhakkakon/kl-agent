import subprocess
from Xlib import display

try:
    from ewmh import EWMH
    EWMH_AVAILABLE = True
except ImportError:
    EWMH_AVAILABLE = False

class LinuxWindowTitleMethods:
    def try_xdotool(self) -> str:
        try:
            window_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()
            window_name = subprocess.check_output(['xdotool', 'getwindowname', window_id]).decode().strip()
            return window_name
        except:
            return "Unknown"

    def try_wmctrl(self) -> str:
        try:
            cmd = "wmctrl -a :ACTIVE: -v"
            result = subprocess.run(cmd.split(),
                                 capture_output=True,
                                 text=True,
                                 timeout=1)
            if result.returncode == 0:
                for line in result.stdout.splitlines():
                    if "Window manager's title of the active window" in line:
                        return line.split(":")[-1].strip()
        except:
            return "Unknown"

    def try_xlib(self) -> str:
        try:
            d = display.Display()
            window = d.get_input_focus().focus
            wmname = window.get_wm_name()
            return wmname if wmname else "Unknown"
        except:
            return "Unknown"

    def try_ewmh(self) -> str:
        if not EWMH_AVAILABLE:
            return "Unknown"
        try:
            ewmh = EWMH()
            ewmh.display.sync()
            active_window = ewmh.getActiveWindow()
            if active_window:
                window_name = ewmh.getWmName(active_window).decode() if ewmh.getWmName(active_window) else "Unknown"
                return window_name
        except:
            return "Unknown"
        return "Unknown"

    def try_xprop(self) -> str:
        try:
            cmd = "xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d ' ' -f 5) WM_NAME"
            result = subprocess.run(cmd, 
                                 shell=True,
                                 capture_output=True,
                                 text=True,
                                 timeout=1)
            if result.returncode == 0:
                return result.stdout.split("=")[-1].strip().strip('"')
        except:
            return "Unknown"
