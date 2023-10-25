def nic_func(n_1, n_2, n_3):
    counter = 0
    if n_1 < 0:
        counter += 1
    if n_2 < 0:
        counter += 1
    if n_3 < 0:
        counter += 1

    if n_1 == 0 or n_2 == 0 or n_3 == 0:
        return "zero"
    elif counter == 1 or counter == 3:
        return "negative"
    else:
        return "positive"


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(nic_func(num_1, num_2, num_3))
