def output(what_to_buy, how_many_to_buy):
    if what_to_buy == "coffee":
        result = 1.5 * how_many_to_buy
    elif what_to_buy == "water":
        result = 1 * how_many_to_buy
    elif what_to_buy == "coke":
        result = 1.4 * how_many_to_buy
    else:
        result = 2 * how_many_to_buy
    return f"{result:.2f}"


product = input()
quantity_1 = int(input())
print(output(product, quantity_1))
