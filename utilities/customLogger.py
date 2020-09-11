import logging


class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename='.\\Logs\\automation.log', format='%(asctime)s: %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    # @staticmethod
    # def log_gen():
    #
    #     LOG_FILENAME = '.\\Logs\\automation.log'
    #
    #     # Set up a specific logger with our desired output level
    #     my_logger = logging.getLogger('nopCommerce')
    #     my_logger.setLevel(logging.INFO)
    #
    #     # Add the log message handler to the logger
    #     handler = logging.handlers.RotatingFileHandler(
    #         LOG_FILENAME, maxBytes=20, backupCount=5)
    #
    #     my_logger.addHandler(handler)
    #
    #     return my_logger