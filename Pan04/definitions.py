import pathlib
import os

file_data = {
    "user": {
        "file_name": "users.csv",
        "columns": ("id", "first", "last", "password", "position", "salary", "role")
    },
    "car_lot": {
        "file_name": "car_lot.csv",
        "columns": ("id", "employees", "vehicles")
    },
    "vehicle": {
        "file_name": "car_fleet.csv",
        "columns": ("id", "make", "model", "fuel", "last_test", 'first_name', 'last_name')
    }
}


# logger definitions
DEFAULT_LOG_FILE_BASE_DIR = str(pathlib.Path(__file__).parent) + os.sep + "log"
DEFAULT_CSV_FILE_BASE_DIR = str(pathlib.Path(__file__).parent) + os.sep + "car-fleet"
USER_CSV_FILE_BASE_DIR = str(pathlib.Path(__file__).parent)
TIME_MSG_FORMAT = "%m-%d-%Y, %H:%M:%S"
TIME_FILE_FORMAT = "%H_%M_%S"
