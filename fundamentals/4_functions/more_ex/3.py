def closest_point(x1, y1, x2, y2):
    def distance_from_center(x, y):
        return ((x ** 2) + (y ** 2)) ** 0.5

    d1 = distance_from_center(x1, y1)
    d2 = distance_from_center(x2, y2)

    if d1 <= d2:
        return [x1, y1]
    else:
        return [x2, y2]


def longer(x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    d2 = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5

    if d1 >= d2:
        start_point = closest_point(x1, y1, x2, y2)
        end_point = [x2, y2] if [x2, y2] != start_point else [x1, y1]
    else:
        start_point = closest_point(x3, y3, x4, y4)
        end_point = [x4, y4] if [x4, y4] != start_point else [x3, y3]

    start_x, start_y = start_point
    end_x, end_y = end_point

    return "({}, {})({}, {})".format(int(start_x), int(start_y), int(end_x), int(end_y))


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())
print(longer(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4))
