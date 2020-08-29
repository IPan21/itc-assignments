import definitions
from filehandler import FileHandler
import csv
import os
from logger import Logger
from csv import DictWriter
log = Logger


class User:
    def __init__(self):
        self.csv_path = definitions.USER_CSV_FILE_BASE_DIR + os.sep + "users.csv"
        vehicle_file_handler = FileHandler(self.csv_path)
        self.__users = vehicle_file_handler.get_data()

    def user_auth(self, name, password):
        try:
            name_column_index = definitions.file_data.get("user").get("columns").index("first")
            password_column_index = definitions.file_data.get("user").get("columns").index("password")
            role_column_index = definitions.file_data.get("user").get("columns").index("role")
            for row in self.__users:
                if name == row[name_column_index] and password == row[password_column_index]:
                    print("name and password are correct")
                    # print(row)
                    if row[role_column_index]:
                        print(row[role_column_index])
                        return row[role_column_index]
                    else:
                        return False
            print('wrong name or password')
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def add_user(self, row_id, **kwargs):
        try:
            id_column_index = definitions.file_data.get("user").get("columns").index("id")
            data_field_names = [kwargs.keys()]
            fields_list = [i for i in kwargs.keys()]
            values_list = [i for i in kwargs.values()]
            # get the csv field names
            with open(self.csv_path, 'r') as f:
                d_reader = csv.DictReader(f)
                field_names = d_reader.fieldnames
                # compare
                if fields_list == field_names:
                    for row in d_reader:
                        if int(row['id']) == row_id or int(row['id']) == values_list[id_column_index]:
                            print('this id already exists')
                            Logger.add_to_log('this id already exists')
                            return False
                    with open(self.csv_path, 'a+') as writeFile:
                        writer = csv.writer(writeFile)
                        writer.writerow(values_list)
                        return True
                else:
                    print("data field names don't match")
                    return False
        except Exception as e:
            print(e)
            Logger.add_to_log(e)


user = User()

# new_row = {'id': 9, 'first': 'Irina', 'last': 'Pan', 'password': 'pass5', 'position': 'producer', 'salary': 50000, 'role': 'five'}
# row_dict = {'Id': 81, 'Name': 'Sachin', 'Course':'Maths', 'City':'Mumbai', 'Session':'Evening'}
# user.add_user(10, **new_row)
# user.add_user(4, **row_dict)
# user.user_auth("Donald", "pass4")

# User.user_auth("Donald", "pass4")
# User.user_auth(56, "pass4")

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
