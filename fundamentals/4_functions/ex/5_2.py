def my_func(string):
    result = []
    string = [int(x) for x in string]
    for i in string:
        if i % 2 == 0:
            result.append(i)
    return result


word = input().split()
print(my_func(word))
