def my_func(nikey):
    nikey = [abs(float(x)) for x in nikey]
    return nikey


my_list = input().split()
print(my_func(my_list))
