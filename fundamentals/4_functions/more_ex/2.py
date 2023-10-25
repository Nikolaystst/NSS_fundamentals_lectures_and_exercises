from math import sqrt


def closest_point(x1, y1, x2, y2):
    result = sqrt((x1 ** 2) + (y1 ** 2))
    result_2 = sqrt((x2 ** 2) + (y2 ** 2))
    if result <= result_2:
        return f"({int(x1)}, {int(y1)})"
    else:
        return f"({int(x2)}, {int(y2)})"


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(closest_point(x_1, y_1, x_2, y_2))
