import definitions
import csv
import os
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
                reader = csv.reader(f)
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


car_csv = definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + 'car_fleet.csv'
CarLot.get_all_cars_by_brand(car_csv, "Opel")

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




