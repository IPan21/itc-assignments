import logging


class Logger:
    @staticmethod
    def add_to_log(msg):
        try:
            logging.basicConfig(filename="logfile.log", level=logging.DEBUG, format='%(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.debug(msg)
        except Exception as e:
            print(e)