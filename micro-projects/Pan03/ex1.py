# #
# import csv
# from csv import reader
#
#
# class CarLot:
#     floors = 0
#     total_spots = 0
#
#     def __init__(self, floors, total_spots):
#         self.floors = floors
#         self.total_spots = total_spots
#
#     def set_floors(self, floors):
#         try:
#             int(floors)
#             self.floors = floors
#         except ValueError:
#             print("not an integer")
#         return self.floors
#
#     def set_total_spots(self, total_spots):
#         try:
#             int(total_spots)
#             self.total_spots = total_spots
#         except ValueError:
#             print("not an integer")
#         return self.total_spots
#
#     def get_floors(self):
#         return self.floors
#
#     def get_floors(self):
#         return self.floors
#
#
# cars_lot = CarLot(50, 20)
# cars_lot.set_floors(5)
#
# print(cars_lot.get_floors())
#
#
# class Vehicle:
#     fuel = "diesel"
#     overall_mass = 0
#
#     def __init__(self, fuel, overall_mass):
#         self.fuel = fuel
#         self.overall_mass = self.set_overall_mass(overall_mass)
#
#     def set_fuel(self, fuel):
#         self.fuel = fuel
#
#     def set_overall_mass(self, overall_mass):
#         try:
#             int(overall_mass)
#             self.overall_mass = overall_mass
#         except ValueError:
#             print("not an integer")
#         return self.overall_mass
#
#     def get_fuel(self):
#         return self.fuel
#
#     def get_overall_mass(self):
#         return self.overall_mass
#
#
#     @staticmethod
#     def load_from_csv(path):
#         with open(path, 'r') as csv_file:
#             csv_reader = csv.DictReader(csv_file, fieldnames=['make', 'model'])
#             next(csv_reader, None)
#             for column in csv_reader:
#                 print(f'\t{column["make"]} {column["model"]}')
#
#
# vehicle = Vehicle("diesel", 20)
# vehicle.set_overall_mass(60)
# print(vehicle.get_overall_mass())
# Vehicle.load_from_csv("models.csv")
#
#
#
# class Bike(Vehicle):
#     has_third_wheel = True
#
#     def __init__(self, make, model, third_wheel, fuel, overall_mass):
#         self.make = make
#         self.model = model
#         self.has_third_wheel = third_wheel
#         super().__init__(fuel, overall_mass)
#
#     def does_have_third_wheel(self):
#         return self.has_third_wheel
#
#
# bike = Bike("Honda", "CX", True, "gasoline", 500)
# bike.set_overall_mass(400)
# print(bike.set_overall_mass("abc"))
# print(bike.does_have_third_wheel())
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, fuel, overall_mass):
#         self.make = make
#         self.model = model
#         super().__init__(fuel, overall_mass)
#
#     @staticmethod
#     def load_from_csv(path):
#         with open(path, 'r') as read_obj:
#             car_list = []
#             csv_read = reader(read_obj)
#             for row in csv_read:
#                 car_list.append(row)
#             print(car_list)
#
#
# car = Car("Volvo", "CX", "gasoline", 500)
# car.set_overall_mass(300)
# print(car.fuel)
# print(car.set_overall_mass("abc"))
# Car.load_from_csv('models.csv')
