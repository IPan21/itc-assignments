

def build_pyramid_with_given_height_and_direction(height, direction="up"):
    try:
        if isinstance(height, int) and height > 0 and direction == "up":
            spaces = 3 * height - 2
            for i in range(0, height):
                for j in range(0, spaces):
                    print(end=" ")
                spaces = spaces - 1
                for j in range(0, i + 1):
                    print("* ", end="")
                print("\r")
        elif isinstance(height, int) and height > 0 and direction == "down":
            spaces = 3 * height - 2
            for i in range(height, 0, -1):
                for j in range(0, spaces):
                    print(end=" ")
                spaces = spaces + 1
                for j in range(0, i):
                    print("* ", end="")
                print("\r")
        else:
            print('invalid')
            return False
    except ValueError:
        print('invalid input')
        return False


build_pyramid_with_given_height_and_direction(5, "down")