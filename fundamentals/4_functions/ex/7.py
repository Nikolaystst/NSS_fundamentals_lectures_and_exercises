def output(n_1):
    my_list = n_1.split()
    my_list = [int(x) for x in my_list]
    result_1 = min(my_list)
    result_2 = max(my_list)
    result_3 = sum(my_list)
    print(f"The minimum number is {result_1}")
    print(f"The maximum number is {result_2}")
    print(f"The sum number is: {result_3}")


num_1 = input()
output(num_1)
