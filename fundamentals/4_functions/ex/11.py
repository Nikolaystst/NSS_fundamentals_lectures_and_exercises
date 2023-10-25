def nic_func(n_1):
    result = int(num / 10)
    result_2 = 10 - result
    my_list = result * "%" + result_2 * "."
    if n_1 == 100:
        print(f"{n_1}% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{n_1}% [{my_list}]")
        print("Still loading...")


num = int(input())
nic_func(num)
