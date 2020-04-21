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

    @staticmethod
    def user_auth(name, password):
        try:
            with open("users.csv", "r") as f:
                readers = csv.DictReader(f, delimiter=",")
                for row in readers:
                    if name == row['first'] and password == row['password']:
                        print("name and password are correct")
                        if row['role']:
                            return row['role']
                        else:
                            return False
                print('wrong name or password')
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def add_user(self, row_id, **kwargs):
        try:
            id_column_index = definitions.file_data.get("user").get("columns").index("user_id")
            print(id_column_index)
            data_field_names = [kwargs.keys()]
            fields_list = [i for i in kwargs.keys()]
            print(fields_list)
            print(row_id)
            data = [kwargs.values()]
            # get the csv field names
            with open(self.csv_path, 'r') as f:
                d_reader = csv.DictReader(f)
                field_names = d_reader.fieldnames
                # compare
                if fields_list == field_names:
                    for row in d_reader:
                        print(row_id)
                        # print(int(row[id_column_index]))
                        print('hi')
                        if int(row[id_column_index]) == row_id:
                            print('this user_id already exists')
                            Logger.add_to_log('this user_id already exists')
                            return False
                        else:
                            print('hi')
                    print('hi')
                    with open(self.csv_path, 'a+', newline='') as write_obj:
                        dict_writer = DictWriter(write_obj, fieldnames=field_names)
                        dict_writer.writerow(data)
                        print('hi')
                        return True
                else:
                    print("data field names don't match")
                    return False
        except Exception as e:
            print(e)
            Logger.add_to_log(e)


user = User()

new_row = {'user_id': 9, 'first': 'Irina', 'last': 'Pan', 'password': 'pass5', 'position': 'producer', 'salary': 50000, 'role': 'five'}
row_dict = {'Id': 81, 'Name': 'Sachin', 'Course':'Maths', 'City':'Mumbai', 'Session':'Evening'}
user.add_user(9, **new_row)
# user.add_user(4, **row_dict)


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
