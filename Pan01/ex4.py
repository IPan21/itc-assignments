

input_ex4 = input('Enter a number to check if it is parsable: ')


def is_parsable(my_input):
    try:
        if isinstance(my_input, int) or isinstance(int(my_input), int):
            print('Yep!')
            return True
        else:
            return False
    except ValueError:
        return False


print(is_parsable(input_ex4))

# print(is_parsable(4))
# print(is_parsable('4'))
# print(is_parsable('4.5'))
# print(is_parsable('abc'))
