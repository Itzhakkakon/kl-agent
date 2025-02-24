from factories.writer_factory import WriterFactory
from factories.key_logger_factory import KeyLoggerFactory

def main():
    writer = WriterFactory.create_writer("file", "keylog.txt")
    logger = KeyLoggerFactory.create_logger(writer)
    
    try:
        print("Press Esc to stop logging...")
        logger.start()
    finally:
        logger.stop()
        writer.close()
    
if __name__ == "__main__":
    main()