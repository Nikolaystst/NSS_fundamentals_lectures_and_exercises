def nic_func(n_1, n_2):
    result = 1
    result_2 = 1
    for i in range(1, int(n_1) + 1):
        result *= i
    for i in range(1, int(n_2) + 1):
        result_2 *= i
    return f"{(result / result_2):.2f}"


num_1 = int(input())
num_2 = int(input())
print(nic_func(num_1, num_2))
