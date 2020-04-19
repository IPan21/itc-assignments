
import logging
import csv
from csv import reader
from csv import writer
from csv import DictWriter
from logger import Logger


class FileHandler:

    @staticmethod
    def load_from_csv(file_name):
        try:
            with open(file_name, 'r') as read_obj:
                # car_list = []
                csv_read = reader(read_obj)
                for row in csv_read:
                    print(row)
                #     car_list.append(row)
                # print(car_list)
        except Exception as e:
            print(e)
            Logger.add_to_log(e)


    @staticmethod
    def append_to_csv(file_name, data):
        try:
            # get the data field names
            data_field_names = []
            for key in data.keys():
                data_field_names.append(key)
            # get the csv field names
            with open(file_name, 'r') as f:
                d_reader = csv.DictReader(f)
                field_names = d_reader.fieldnames
            # compare
                if data_field_names == field_names:
                    for row in d_reader:
                        if int(row['user_id']) == data['user_id']:
                            print('this user_id already exists')
                            Logger.add_to_log('this user_id already exists')
                            return False

                    with open(file_name, 'a+', newline='') as write_obj:
                        dict_writer = DictWriter(write_obj, fieldnames=field_names)
                        dict_writer.writerow(data)
                        return True
                else:
                    print("data field names don't match")
                    return False
        except Exception as e:
            print(e)
            Logger.add_to_log(e)


new_row = {'user_id': 8, 'first': 'Irina', 'last': 'Pan', 'password': 'pass5', 'position': 'producer', 'salary': 50000, 'role': 'five'}
row_dict = {'Id': 81, 'Name': 'Sachin', 'Course':'Maths', 'City':'Mumbai', 'Session':'Evening'}

# FileHandler.load_from_csv('users.csv')
FileHandler.append_to_csv('users.csv', new_row)
# FileHandler.append_to_csv('users.csv', row_dict)