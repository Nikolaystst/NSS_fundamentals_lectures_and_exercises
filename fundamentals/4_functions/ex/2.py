def sum_numbers(first, second):
    result = first + second
    return result


def subtract(one, two):
    result = one - two
    return result


def add_and_subtract(one, two, three):
    result = (one + two) - three
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result = sum_numbers(num_1, num_2)

print(subtract(result, num_3))
