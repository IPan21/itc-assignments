

num_of_rows = 5


def build_pyramid(num_of_rows):
    spaces = 3*num_of_rows - 2
    for i in range(0, num_of_rows):
        for j in range(0, spaces):
            print(end=" ")
        spaces = spaces - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


build_pyramid(num_of_rows)
