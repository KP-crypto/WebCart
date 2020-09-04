import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:/Users/Acer/PycharmProjects/wpmobil/Logs/ketan.txt",
                            format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger





