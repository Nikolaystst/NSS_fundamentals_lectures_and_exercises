items_prices = input().split("|")
budget = float(input())
profit = 0
profit_for_budget = 0

for i in items_prices:
    type_value = i.split("->")
    type_of_cloth = type_value[0]
    value_of_cloth = float(type_value[1])

    if type_of_cloth == "Clothes" and (0 > value_of_cloth or value_of_cloth > 50):
        continue

    if type_of_cloth == "Shoes" and (0 > value_of_cloth or value_of_cloth > 35):
        continue

    if type_of_cloth == "Accessories" and (0 > value_of_cloth or value_of_cloth > 20.5):
        continue

    if budget >= value_of_cloth:
        budget -= value_of_cloth
        new_price = 1.4 * value_of_cloth
        print(f"{new_price:.2f}", end=" ")
        profit += 0.4 * value_of_cloth
        profit_for_budget += 1.4 * value_of_cloth
    else:
        continue

print()
print(f"Profit: {profit:.2f}")

budget += profit_for_budget

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
