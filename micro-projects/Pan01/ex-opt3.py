

def solve_math(math_string, first, second, third, fourth, fifth):
    new_string = ""
    new_list = [first, second, third, fourth, fifth]
    list_index = 0
    for i in range(0, len(math_string)):
        if math_string[i] == "x":
            new_string = new_string + str(new_list[list_index])
            list_index = list_index + 1
        else:
            new_string = new_string + str(math_string[i])
    result = eval(new_string)
    print(result)
    return result


solve_math("x*x-x/x+x", 1, 2, 3, 4, 5)
