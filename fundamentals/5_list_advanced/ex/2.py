def my_func(lst):
    lst = [int(x) for x in lst]
    if lst[2] < 9:
        lst[2] += 1
    else:
        lst[2] = 0
        if lst[1] < 9:
            lst[1] += 1
        else:
            lst[1] = 0
            lst[0] += 1
    lst = [str(x) for x in lst]
    return ".".join(lst)


version = input().split(".")
print(my_func(version))
