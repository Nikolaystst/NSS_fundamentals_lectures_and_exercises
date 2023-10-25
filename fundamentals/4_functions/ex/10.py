def output(n_1):
    divisors = [i for i in range(1, n_1) if n_1 % i == 0]
    aliquot_sum = sum(divisors)
    if aliquot_sum == n_1:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

num = int(input())
print(output(num))
