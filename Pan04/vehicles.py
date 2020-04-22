from filehandler import FileHandler
import csv
import definitions
import os
from logger import Logger

log = Logger


class Vehicle:

    def __init__(self):
        self.csv_path = definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + "car_fleet.csv"
        vehicle_file_handler = FileHandler(definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + "car_fleet.csv")
        self.__vehicles = vehicle_file_handler.get_data()

    def print(self):
        print(self.__vehicles)

    def update_csv(self, row_id, **kwargs):
        try:
            previous_lines = self.__vehicles
            lines = list()
            id_column_index = definitions.file_data.get("vehicle").get("columns").index("id")
            for row in self.__vehicles:
                if row[id_column_index] != str(row_id):
                    lines.append(row)
                elif row[id_column_index] == str(row_id):
                    lines.append(kwargs.values())
            with open(self.csv_path, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
            if lines != previous_lines:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            Logger.add_to_log(e)

###uncomment to check update_csv
# vehicle = Vehicle()
# row_dict = {'id': 4, 'make': 'Skoda', 'model':'Yeti', 'fuel':'gasoline', 'last_test':'04/1/2020'}
# vehicle.update_csv(4, **row_dict)


# import definitions
# from file_handler import FileHandler


# class Users:
#     __users = []
#
#     def __init__(self):
#         user_file_handler = FileHandler("user.csv")
#         self.__users = user_file_handler.get_data()
#
#     def user_auth(self, name, password):
#         try:
#             name_columns_pos = definitions.file_data.get("user").get("columns").index("first_name")
#             password_column_pos = definitions.file_data.get("user").get("columns").index("password")
#             role_column_pos = definitions.file_data.get("user").get("columns").index("role")
#
#             for user in self.__users:
#                 if user[name_columns_pos] == name and user[password_column_pos] == password:
#                     return user[role_column_pos]
#
#             return False
#         except Exception as e:
#             raise Exception("error, unable to authenticate {} with password {}".format(name, password))
