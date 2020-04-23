
# ############ DAY 1, OPTIONAL EXERCISE LOGGER VERSION ##############

import definitions
import logging
import os
import time
import glob
import datetime


class Logger:
    def __init__(self):
        self.path = definitions.DEFAULT_LOG_FILE_BASE_DIR

    def remove_old_files(self):
        # remove files created more than 24 hours ago
        now = time.time()
        for f in os.listdir(self.path):
            f = os.path.join(self.path, f)
            if os.stat(f).st_birthtime < now - 1 * 86400:
                if os.path.isfile(f):
                    os.remove(f)

    def add_to_log(self, msg):
        self.remove_old_files()
        now = time.time()
        path = self.path
        date = datetime.datetime.now()
        # finds the latest file
        list_of_files = glob.glob(path + '/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        # if it exists less than an hour, append log message
        if os.stat(latest_file).st_birthtime > now - 1 * 3600:
            logging.basicConfig(filename=latest_file, level=logging.DEBUG, format='%(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.debug(msg)
            print("hi1")
        else:
            # create a new file, append log message
            date_now = date.strftime("%d-%m-%Y_%H-%M-%S")
            logging.basicConfig(filename=path + os.sep + "logfile" + date_now + ".log",
                                level=logging.DEBUG,
                                format='%(asctime)s %(name)s %(levelname)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.debug(msg)
            print("hi2")


# test_log = Logger()
# test_log.add_to_log("TEST_MESSAGE")


# ############ DAY 1, EXERCISE 5 LOGGER VERSION ##############


# import logging
# import definitions
# import os
#
#
# class Logger:
#     @staticmethod
#     def add_to_log(msg):
#         try:
#             path = definitions.DEFAULT_LOG_FILE_BASE_DIR
#             logging.basicConfig(filename=path + os.sep + "logfile.log",
#                                 level=logging.DEBUG,
#                                 format='%(asctime)s %(message)s',
#                                 datefmt='%m/%d/%Y %I:%M:%S %p')
#             logging.debug(msg)
#         except Exception as e:
#             print(e)
#
#
# Logger.add_to_log("TEST")
