def output(func, first, second):
    if func == "multiply":
        result = first * second
    elif func == "divide":
        result = int(first / second)
    elif func == "add":
        result = first + second
    else:
        result = first - second
    return result


math_func = input()
first_int = int(input())
second_int = int(input())
print(output(math_func, first_int, second_int))
