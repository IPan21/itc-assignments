import definitions
import csv
import os
from filehandler import FileHandler
from datetime import datetime
from dateutil.relativedelta import relativedelta
import datetime
import dateutil.relativedelta
from csv import reader
import pandas as pd
from csv import writer
from csv import DictWriter
from logger import Logger
import fileinput


log = Logger
# car_csv_dir = DEFAULT_CSV_FILE_BASE_DIR
# print(car_csv_dir)


class CarLot:

    def __init__(self):
        self.car_csv = definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + 'car_fleet.csv'
        vehicle_file_handler = FileHandler(definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + "car_fleet.csv")
        self.__vehicles = vehicle_file_handler.get_data()
        self.csv_path = definitions.USER_CSV_FILE_BASE_DIR + os.sep + "users.csv"
        vehicle_file_handler = FileHandler(self.csv_path)
        self.__users = vehicle_file_handler.get_data()

    @staticmethod
    def update_salary_by_name(file_name, employee_salary, name):
        try:
            lines = list()
            with open(file_name, 'r') as readFile:
                readers = csv.reader(readFile)
                for row in readers:
                    if row[1] != name:
                        lines.append(row)
                    elif row[1] == name:
                        row[5] = employee_salary
                        lines.append(row)
            with open(file_name, 'w') as writeFile:
                writers = csv.writer(writeFile)
                writers.writerows(lines)
        except Exception as e:
            print(e)
            log.add_to_log(e)

    @staticmethod
    def add_to_fleet(external_csv_fleet_file, internal_csv):
        try:
            with open(external_csv_fleet_file, "r") as f:
                readers = csv.reader(f)
                ex_headers = next(reader)
            with open(internal_csv, "r") as f:
                reader = csv.reader(f)
                headers = next(reader)
            if headers != ex_headers:
                print('wrong csv format')
                log.add_to_log('wrong csv format')
                return False

            f1 = open(external_csv_fleet_file, 'r').readlines()
            f2 = open(internal_csv, 'r').readlines()
            f = open(internal_csv, 'a')
            for _ in range(2):
                for row in f1:
                    if row not in f2:
                        f.write(row)
                f1, f2 = f2, f1
            return True
        except Exception as e:
            print(e)
            log.add_to_log(e)

    @staticmethod
    def get_fleet_size(file_name):
        try:
            file = open(file_name)
            reader = csv.reader(file)
            lines = len(list(reader))
            print(str(lines - 1) + ' cars')
        except Exception as e:
            print(e)
            log.add_to_log(e)

    @staticmethod
    def get_all_cars_by_brand(file_name, brand):
        try:
            make_column_index = definitions.file_data.get("vehicle").get("columns").index("make")
            lines = list()
            with open(file_name, 'r') as readFile:
                readers = csv.reader(readFile)
                for row in readers:
                    if row[make_column_index] == brand:
                        lines.append(row)
                print(len(lines))
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def get_all_cars_by_filter(self, and_or="OR", **kwargs):
        try:
            lines = list()
            for row in self.__vehicles:
                count = 0
                for keys, values in kwargs.items():
                    column_index = definitions.file_data.get("vehicle").get("columns").index(keys)
                    if row[column_index] == values:
                        count += 1
                if count > 0 and and_or == "OR":
                    lines.append(row)
                elif count == len(kwargs):
                    lines.append(row)
            print(lines)
            if len(lines) > 0:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def get_time_to_test(self, _id):
        try:
            column_index = definitions.file_data.get("vehicle").get("columns").index('id')
            test_column_index = definitions.file_data.get("vehicle").get("columns").index('last_test')
            count = 0
            for item in self.__vehicles:
                if item[column_index] == str(_id):
                    test_date_string = item[test_column_index]
                    format_string = "%m/%d/%Y"
                    new_format_string = "%Y, %m, %d"
                    datetime_object = datetime.datetime.strptime(test_date_string, format_string).date()
                    new_date = datetime_object + relativedelta(years=1)
                    new_date_string = datetime.datetime.strftime(new_date, new_format_string).replace(' 0', ' ')
                    m_list = [int(e) for e in new_date_string.split(',')]
                    today = datetime.date.today()
                    future = datetime.date(m_list[0], m_list[1], m_list[2])
                    diff = future - today
                    count += 1
            if count == 1:
                print('Next test in ' + str(diff.days) + ' days')
                return diff.days
            else:
                print('id doesn’t exist or no test time defined for vehicle')
                return False
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def how_many_own_more_then_one_car(self):
        try:
            first_index = definitions.file_data.get("vehicle").get("columns").index('first_name')
            last_index = definitions.file_data.get("vehicle").get("columns").index('last_name')
            id_index = definitions.file_data.get("vehicle").get("columns").index('id')
            owners_list = []
            for j in self.__vehicles:
                for i in self.__vehicles:
                    if (
                            j[first_index] == i[first_index] and
                            j[last_index] == i[last_index] and
                            j[id_index] != i[id_index] and
                            i[first_index] + ' ' + i[last_index] not in owners_list
                    ):
                        owners_list.append(i[first_index] + ' ' + i[last_index])
            if len(owners_list) > 0:
                print(str(len(owners_list)) + ' owners own more than one car')
                print(owners_list)
                return owners_list
            else:
                return False
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def does_employee_have_car(self):
        try:
            first_index = definitions.file_data.get("vehicle").get("columns").index('first_name')
            last_index = definitions.file_data.get("vehicle").get("columns").index('last_name')
            first_index_u = definitions.file_data.get("user").get("columns").index('first')
            last_index_u = definitions.file_data.get("user").get("columns").index('last')
            print()
            employees_list = []
            for j in self.__vehicles:
                for i in self.__users:
                    if (
                            j[first_index] == i[first_index_u] and
                            j[last_index] == i[last_index_u] and
                            i[first_index_u] + ' ' + i[last_index_u] not in employees_list
                    ):
                        # print(j[first_index] + ' ' + j[last_index])
                        employees_list.append(j)
            if len(employees_list) > 0:
                # print(str(len(employees_list)) + ' employees own a car')
                return employees_list
            else:
                return False
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def get_all_employee_who_own_car_brand(self, brand):
        try:
            employees_own_cars_list = self.does_employee_have_car()
            brand_index = definitions.file_data.get("vehicle").get("columns").index('make')
            car_brand_owners_list = []
            for i in employees_own_cars_list:
                if i[brand_index] == brand:
                    car_brand_owners_list.append(i)
            print(car_brand_owners_list)
            if len(car_brand_owners_list) > 0:
                return car_brand_owners_list
            else:
                return False
        except Exception as e:
            print(e)
            log.add_to_log(e)


#CarLot.get_all_employee_who_ own_car_brand(brand)
#Details: This function searches for matches between car owners and employees who own a car with vehicle of brand = <brand>
#Return val: list of employees who own cars of type brand in the lot false if non do.
#Error handling: Throws (bubbels) Errors if exist

cars_lot = CarLot()
cars_lot.get_all_employee_who_own_car_brand("Skoda")
# cars_lot.does_employee_have_car()
# cars_lot.get_time_to_test(10)

# cars_lot.how_many_own_more_then_one_car()

# key_arguments = {"make":"Skoda", "mode":"Yeti"}
# cars_lot.get_all_cars_by_filter(and_or="OR", make="Skoda", model="Yeti")

# uncomment to check get_all_cars_by_brand
# car_csv = definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + 'car_fleet.csv'
# CarLot.get_all_cars_by_brand(car_csv, "Opel")

# uncomment to check update_salary_by_name
# name_to_update = 'Irina'
# CarLot.update_salary_by_name('users.csv', '80000', name_to_update)

# uncomment to check update_salary_by_name
# external = 'car-fleet/external_car_fleet.csv'
# internal = 'car-fleet/car_fleet.csv'
# CarLot.add_to_fleet(external, internal)

# uncomment to check get_fleet_size
# internal = 'car-fleet/car_fleet.csv'
# CarLot.get_fleet_size(internal)




