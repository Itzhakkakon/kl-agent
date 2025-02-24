import subprocess
import time

def get_title_xdotool():
    try:
        window_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()
        window_name = subprocess.check_output(['xdotool', 'getwindowname', window_id]).decode().strip()
        return window_name
    except Exception as e:
        return f"Error: {e}"

def get_title_wmctrl():
    try:
        cmd1 = "xprop -root _NET_ACTIVE_WINDOW"
        output = subprocess.check_output(cmd1, shell=True).decode()
        window_id = output.split()[-1]
        
        cmd2 = f"xprop -id {window_id} WM_NAME"
        output = subprocess.check_output(cmd2, shell=True).decode()
        return output.split('=')[-1].strip().strip('"')
    except Exception as e:
        return f"Error: {e}"

def get_title_simple():
    try:
        window_id = subprocess.check_output("xdotool getactivewindow".split()).decode().strip()
        window_name = subprocess.check_output(f"xdotool getwindowname {window_id}".split()).decode().strip()
        return window_name
    except:
        return "No window found"

def get_title_ewmh():
    from ewmh import EWMH
    try:
        ewmh = EWMH()
        ewmh.display.sync()
        
        active_window = ewmh.getActiveWindow()
        if active_window:
            window_name = ewmh.getWmName(active_window).decode() if ewmh.getWmName(active_window) else "Unknown"
            return window_name
        return "No active window found"
    except Exception as e:
        return f"Error: {e}"

def main():
    methods = {
        '1': ('XDoTool', get_title_xdotool),
        '2': ('WMCtrl', get_title_wmctrl),
        '3': ('Simple', get_title_simple),
        '4': ('EWMH', get_title_ewmh)
    }
    
    print("Choose a method to detect window title:")
    for key, (name, _) in methods.items():
        print(f"{key}: {name}")
    
    choice = input("Enter number (1-4): ")
    if choice not in methods:
        print("Invalid choice")
        return
    
    print(f"\nUsing {methods[choice][0]} method. Press Ctrl+C to stop.")
    while True:
        try:
            print(methods[choice][1]())
            time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
