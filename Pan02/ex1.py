

# exercise 1

# import datetime
#
# try:
#     try:
#         f = open("my_log", "a")
#     except OSError as e:
#         print("something went wrong: " + e.strerror)
#     x = datetime.datetime.now()
#     f.write(x.strftime("%d/%m/%Y, %H:%M:%S") + " log something or another \n")
# except Exception as e:
#     print(e)


# exercise 2

# words_list = ["angry", "hello", "world", "animal", "acid", "rock"]
# words_list = [i + " hello" if i.startswith("a") else i for i in words_list]
# print(words_list)


# exercise 3

#
# def list_square_even_power_odd(list_range):
#     try:
#         if list_range <= 0:
#             print("range must be bigger than 0")
#         else:
#             words_list = [i ** i if (i % 2) == 0 else i ** 2 for i in range(list_range)]
#             print(words_list)
#     except Exception as e:
#         print(e)
#
#
# list_square_even_power_odd(6)


# exercise 4


# names_list = ["Elton John", "Meredith", "Megan Fox", "Jodie Foster", "Alan"]
#
#
# def name_checker(list_of_names):
#     return list((i for i in list_of_names if ' ' not in i))
#
#
# print(name_checker(names_list))


# exercise 5

# When would the use of generators be preferred over list comprehension and vice versa?
# If you want to store and use the generated results, then it is better to use list comprehension.
# But if generated list is used once - generators are preferable.
# Generators don't support list methods. So if you need to use index or slice - use lists.
# So it depends on what you do. lists reserve memory, but run with less iterations, they are faster.
# generators - opposite.


# optional exercise 1


# import cmath
#
#
# first = float(input('Enter a: '))
# second = float(input('Enter b: '))
# third = float(input('Enter c: '))
#
#
# def get_roots(a, b, c):
#     if b ** 2 <= 4 * a * c:
#         print('discriminant is less than zero')
#         return
#     else:
#         d = (b ** 2) - (4 * a * c)
#         sol1 = lambda e, f, g: (-f - cmath.sqrt(g)) / (2 * e)
#         print("first solution")
#         print(sol1(a, b, c))
#         sol2 = lambda e, f, g: (-f + cmath.sqrt(g)) / (2 * e)
#         print("second solution")
#         print(sol2(a, b, d))
#
#
# get_roots(first, second, third)


# optional exercise 2

# import os
#
#
# def get_list_of_files(dir_name):
#     list_of_files = os.listdir(dir_name)
#     all_files = list()
#     for entry in list_of_files:
#         full_path = os.path.join(dir_name, entry)
#         if os.path.isdir(full_path):
#             all_files = all_files + get_list_of_files(full_path)
#         else:
#             all_files.append(full_path)
#     return all_files
#
#
# dirName = '/Users/ipan/PycharmProjects/daily_1';
# print(get_list_of_files(dirName))
