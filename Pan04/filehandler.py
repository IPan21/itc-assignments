import csv
from csv import reader
import operator
import definitions
from csv import DictWriter
from logger import Logger
log = Logger


class FileHandler:
    __csv_data = None
    row_count = 0

    def __init__(self, csv_file_name):
        if self.__csv_data is None:
            self.__csv_data = []
        self.log = Logger()
        self.load_from_csv(csv_file_name)

    def get_data(self):
        return self.__csv_data

    def load_from_csv(self, file_name):
        try:
            with open(file_name, 'r') as read_obj:
                csv_list = []
                csv_read = reader(read_obj)
                for row in csv_read:
                    # print(row)
                    csv_list.append(row)
                    self.__csv_data.append(row)
                # print(csv_list)
                return csv_list
        except Exception as e:
            print(e)
            log.add_to_log(e)


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
                        if int(row['id']) == data['id']:
                            print('this id already exists')
                            Logger.add_to_log('this id already exists')
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
            log.add_to_log(e)


    @staticmethod
    def remove_from_csv(file_name, row_id):
        try:
            lines = list()
            with open(file_name, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row[0] != str(row_id):
                        lines.append(row)
            with open(file_name, 'w') as writeFile:
                writers = csv.writer(writeFile)
                writers.writerows(lines)
        except Exception as e:
            print(e)
            Logger.add_to_log(e)


    @staticmethod
    def update_csv(file_name, row_id, upd_row):
        try:
            lines = list()
            # field_names = reader.fieldnames
            with open(file_name, 'r') as readFile:
                reader = csv.reader(readFile)
                for row in reader:
                    if row[0] != str(row_id):
                        lines.append(row)
                    elif row[0] == str(row_id):
                        lines.append(upd_row.values())
            with open(file_name, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
        except Exception as e:
            print(e)
            Logger.add_to_log(e)

    @staticmethod
    def sort_by_key(file_name, this_key, direction):
        try:
            lines = list()
            name_columns_pos = definitions.file_data.get("user").get("columns").index(this_key)
            with open(file_name, 'r') as readFile:
                readers = csv.reader(readFile)
                sort = sorted(readers, key=operator.itemgetter(name_columns_pos), reverse=direction)
                for row in sort:
                    if row[name_columns_pos] == this_key:
                        lines.append(row)
                for row in sort:
                    if row[name_columns_pos] != this_key:
                        lines.append(row)
            with open(file_name, 'w') as writeFile:
                writers = csv.writer(writeFile)
                writers.writerows(lines)
        except Exception as e:
            print(e)
            Logger.add_to_log(e)

# uncomment to check sort_by_key
# FileHandler.sort_by_key('users.csv', 'id', False)

# uncomment to check load_from_csv
# FileHandler.load_from_csv(str(pathlib.Path(__file__).parent) + os.sep + "car-fleet" + os.sep + 'car_fleet.csv')

# uncomment to check append_to_csv
# new_row = {'id': 8, 'first': 'Irina', 'last': 'Pan', 'password': 'pass5', 'position': 'producer', 'salary': 50000, 'role': 'five'}
# row_dict = {'Id': 81, 'Name': 'Sachin', 'Course':'Maths', 'City':'Mumbai', 'Session':'Evening'}
# FileHandler.append_to_csv('users.csv', new_row)
# FileHandler.append_to_csv('users.csv', row_dict)

# uncomment to check remove_from_csv
# FileHandler.remove_from_csv('users.csv', 8)

# uncomment to check uodate_csv
# updated_row = {'id': 7, 'first': 'Irina', 'last': 'Pan', 'password': 'pass5', 'position': 'developer', 'salary': 100000, 'role': 'five'}
# FileHandler.update_csv('users.csv', 7, updated_row)
