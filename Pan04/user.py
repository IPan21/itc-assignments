import definitions
import csv
from logger import Logger
log = Logger


class User:
    def __init__(self):
        self.csv_path = definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + "users.csv"
        user_file_handler = FileHandler(self.csv_path)
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

    def update_csv(self, row_id, **kwargs):
        try:
            previous_lines = self.__users
            lines = list()
            id_column_index = definitions.file_data.get("vehicle").get("columns").index("id")
            for row in self.__users:
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

User.user_auth("Donald", "pass4")
User.user_auth(56, "pass4")

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
