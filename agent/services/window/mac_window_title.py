import Quartz
from interfaces.i_window_title import IWindowTitle

class MacWindowTitle(IWindowTitle):
    """Mac implementation of window title tracking"""

    def get_active_window_title(self) -> str:
        """Get the title of the currently active window on macOS"""
        try:
            # Get the frontmost application
            frontmost_app = Quartz.NSWorkspace.sharedWorkspace().frontmostApplication()
            app_name = frontmost_app.localizedName()
            
            # Get active window information
            options = Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListExcludeDesktopElements
            window_list = Quartz.CGWindowListCopyWindowInfo(options, Quartz.kCGNullWindowID)
            
            # Find the frontmost window of the active application
            for window in window_list:
                owner_name = window.get('kCGWindowOwnerName', '')
                window_name = window.get('kCGWindowName', '')
                
                if owner_name == app_name and window_name:
                    return f"{window_name} - {app_name}"
            
            # If no specific window title is found, return app name
            return app_name
        except Exception as e:
            print(f"Error getting window title: {e}")
            return "Unknown"
