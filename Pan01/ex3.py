def is_even(num):
    if isinstance(num, int):
        if (num % 2) == 0:
            return True
        else:
            return False
    else:
        print('This is not an integer')
        return


print(is_even(4))
print(is_even(5))
print(is_even(4.5))
print(is_even('g'))
