import math


def square(side):
    return math.ceil(side * side)


square_side = float(input(f"Введите длину стороны:"))
print(square(square_side))
