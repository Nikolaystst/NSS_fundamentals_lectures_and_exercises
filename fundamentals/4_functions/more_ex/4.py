def nic_func(n1):
    if n1 == 0:
        print()
    elif n1 == 1:
        print(1)
    elif n1 == 2:
        print(1, 1)
    elif n1 == 3:
        print(1, 1, 2)
    else:
        my_list = [1, 1, 2]
        for i in range(4, n1 + 1):
            numero_1 = my_list[i - 2] + my_list[i - 3] + my_list[i - 4]
            my_list.append(numero_1)
        for i in range(len(my_list)):
            print(my_list[i], end=" ")


num = int(input())
nic_func(num)
