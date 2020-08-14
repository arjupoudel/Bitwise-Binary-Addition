def input_numbers1():
    while True:
        try:
            a = int(input('Enter a number between 0-255: '))
        except ValueError:
            print("You are not allowed to enter string, float or boolean value.")
            continue
        else:
            if a > 255:
                print("You have entered out of range number.")
                continue

            elif a < 0:
                print("You have entered a negative integer. You can only enter positive integer.")
                continue
        break
    return a


def input_numbers2():
    while True:
        try:
            b = int(input('Enter another number between 0-255: '))
        except ValueError:
            print("You are not allowed to enter string, float or boolean value.")
            continue
        else:
            if b > 255:
                print("You have entered out of range number.")
                continue

            elif b < 0 :
                print("You have entered a negative integer. You can only enter positive integer.")
                continue
        break
    return b



