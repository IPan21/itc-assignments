import definitions
import csv
import os
from filehandler import FileHandler
from datetime import datetime
from dateutil.relativedelta import relativedelta
import datetime
from logger import Logger
from user import User

log = Logger()


class CarLot:

    def __init__(self):
        self.car_csv = definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + 'car_fleet.csv'
        self.user = User()
        vehicle_file_handler = FileHandler(definitions.DEFAULT_CSV_FILE_BASE_DIR + os.sep + "car_fleet.csv")
        self.__vehicles = vehicle_file_handler.get_data()
        self.csv_path = definitions.USER_CSV_FILE_BASE_DIR + os.sep + "users.csv"
        vehicle_file_handler = FileHandler(self.csv_path)
        self.__users = vehicle_file_handler.get_data()

    def update_salary_by_name(self, employee_salary, name):
        try:
            password_column_index = definitions.file_data.get("user").get("columns").index("password")
            name_column_index = definitions.file_data.get("user").get("columns").index("first")
            salary_column_index = definitions.file_data.get("user").get("columns").index("salary")
            lines = list()
            for row in self.__users:
                if row[name_column_index] != name:
                    lines.append(row)
                elif row[name_column_index] == name:
                    if self.user.user_auth(row[name_column_index], row[password_column_index]) == 'admin':
                        row[salary_column_index] = employee_salary
                        lines.append(row)
                    else:
                        print("can't update salary. the user should have admin status.")
                        return False
            with open(self.csv_path, 'w') as writeFile:
                writers = csv.writer(writeFile)
                writers.writerows(lines)
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def add_to_fleet(self, external_csv_fleet_file):
        try:
            with open(external_csv_fleet_file, "r") as f:
                readers = csv.reader(f)
                ex_headers = next(readers)
            with open(self.car_csv, "r") as f:
                readers = csv.reader(f)
                headers = next(readers)
            if headers != ex_headers:
                print('wrong csv format')
                log.add_to_log('wrong csv format')
                return False

            f1 = open(external_csv_fleet_file, 'r').readlines()
            f2 = open(self.car_csv, 'r').readlines()
            f = open(self.car_csv, 'a')
            for _ in range(2):
                for row in f1:
                    if row not in f2:
                        f.write(row)
                f1, f2 = f2, f1
            return True
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def get_fleet_size(self):
        try:
            lines = len(list(self.__vehicles))
            print(str(lines - 1) + ' cars')
        except Exception as e:
            print(e)
            log.add_to_log(e)

    def get_all_cars_by_brand(self, brand):
        try:
            make_column_index = definitions.file_data.get("vehicle").get("columns").index("make")
            lines = list()
            for row in self.__vehicles:
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


cars_lot = CarLot()
# cars_lot.update_salary_by_name('90000', 'Meredith')
# cars_lot.add_to_fleet('car-fleet/external_car_fleet.csv')
# cars_lot.get_fleet_size()
# cars_lot.get_all_cars_by_brand("Skoda")
# cars_lot.get_all_cars_by_filter(and_or="OR", make="Skoda", model="Yeti")
# cars_lot.get_time_to_test(10)
# cars_lot.how_many_own_more_then_one_car()
# cars_lot.does_employee_have_car()
# cars_lot.get_all_employee_who_own_car_brand("Skoda")
