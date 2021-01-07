import logging
import sys

class LogGen:

    @staticmethod
    def loggen():

        stdout_handler = logging.StreamHandler(sys.stdout)
        handlers = [stdout_handler]

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename=".//Logs//automation.log",filemode='a',
                            format="%(asctime)s: %(levelname)s: %(message)s",datefmt="%d-%m-%Y %H:%M:%S %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger

