from factories.writer_factory import WriterFactory
from factories.key_logger_factory import KeyLoggerFactory
from pynput.keyboard import Key
import json

def main():
    writer = WriterFactory.create_writer("file", "keylog.json")
    logger = KeyLoggerFactory.create_logger()
    
    should_exit = False
    
    try:
        print("Press Esc to stop logging...")
        logger.start()
        while not should_exit:
            keystrokes = logger.get_logged_keys()
            if keystrokes:
                print(keystrokes)
                
                # Always write the keystrokes to file first
                keystroke_dicts = [k.to_dict() for k in keystrokes]
                writer.write(json.dumps(keystroke_dicts) + "\n")
                
                # Check if Esc key is pressed after writing to file
                if any(k.key == Key.esc for k in keystrokes):
                    print("Esc key pressed. Exiting...")
                    should_exit = True
                
                logger.clear_logged_keys()
    finally:
        logger.stop()
        writer.close()
    
if __name__ == "__main__":
    main()