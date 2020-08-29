# exercise 3


# def is_even(num):
#     if isinstance(num, int):
#         if (num % 2) == 0:
#             return True
#         else:
#             return False
#     else:
#         print('Not an integer')
#         return
#
#
# print(is_even(4))
# print(is_even(5))
# print(is_even(4.5))
# print(is_even('g'))


# exercise 4
#
# input_ex4 = input('Enter a number to check if it is parsable: ')
#
#
# def is_parsable(my_input):
#     try:
#         if isinstance(my_input, int) or isinstance(int(my_input), int):
#             return True
#         else:
#             return False
#     except ValueError:
#         return False
#
#
# print(is_parsable(input_ex4))


# exercise 5

# number_of_rows = 5
#
#
# def build_pyramid(num_of_rows):
#     spaces = 3*num_of_rows - 2
#     for i in range(0, num_of_rows):
#         for j in range(0, spaces):
#             print(end=" ")
#         spaces = spaces - 1
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
#
#
# build_pyramid(number_of_rows)


# optional exercise 1
#
# num_of_rows = 9
#
# def build_pyramid_with_given_height(height):
#     try:
#         if isinstance(height, int) and height > 0:
#             spaces = 3 * height - 2
#             for i in range(0, height):
#                 for j in range(0, spaces):
#                     print(end=" ")
#                 spaces = spaces - 1
#                 for j in range(0, i + 1):
#                     print("* ", end="")
#                 print("\r")
#         else:
#             print('invalid')
#             return False
#     except ValueError:
#         print('invalid input')
#         return False
#
#
# build_pyramid_with_given_height(num_of_rows)


# optional exercise 2


# def build_pyramid_with_given_height_and_direction(height, direction="up"):
#     try:
#         if isinstance(height, int) and height > 0 and direction == "up":
#             spaces = 3 * height - 2
#             for i in range(0, height):
#                 for j in range(0, spaces):
#                     print(end=" ")
#                 spaces = spaces - 1
#                 for j in range(0, i + 1):
#                     print("* ", end="")
#                 print("\r")
#         elif isinstance(height, int) and height > 0 and direction == "down":
#             spaces = 3 * height - 2
#             for i in range(height, 0, -1):
#                 for j in range(0, spaces):
#                     print(end=" ")
#                 spaces = spaces + 1
#                 for j in range(0, i):
#                     print("* ", end="")
#                 print("\r")
#         else:
#             print('invalid')
#             return False
#     except ValueError:
#         print('invalid input')
#         return False
#
#
# build_pyramid_with_given_height_and_direction(3, "down")


# optional exercise 3

# def solve_math(math_string, first, second, third, fourth, fifth):
#     new_string = ""
#     new_list = [first, second, third, fourth, fifth]
#     list_index = 0
#     for i in range(0, len(math_string)):
#         if math_string[i] == "x":
#             new_string = new_string + str(new_list[list_index])
#             list_index = list_index + 1
#         else:
#             new_string = new_string + str(math_string[i])
#     result = eval(new_string)
#     print(result)
#
#
# solve_math("x*x-x/x+x", 1, 2, 3, 4, 5)
