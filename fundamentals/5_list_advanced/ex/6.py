def nic_func(num, my_list):
    for i in range(1, num + 1):
        electrons = 2 * i ** 2
        if num <= (sum(my_list) + electrons):
            my_list.append((num - sum(my_list)))
            break
        else:
            my_list.append(electrons)
    return my_list


num = int(input())
my_list = []
print(nic_func(num, my_list))
