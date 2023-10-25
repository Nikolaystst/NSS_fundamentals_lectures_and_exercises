def sum_even_odd(one_integer):
    sum_of_odd = 0
    sum_of_even = 0
    for i in one_integer:
        if int(i) % 2 == 0:
            sum_of_even += int(i)
        else:
            sum_of_odd += int(i)
    print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")


numero_uno = input()
sum_even_odd(numero_uno)
