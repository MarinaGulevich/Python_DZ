import math


def square(side):
    return math.ceil(side * side)


square_side = int(input(f"Введите длину стороны:"))
print(math.ceil(square(square_side)))
