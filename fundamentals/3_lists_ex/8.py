fires = input().split("#")
water_lvl = int(input())
effort_lvl = 0
fire_lvl = 0

print("Cells:")

for arg in fires:
    type_amount_of_fire = arg.split(" = ")
    type_fire = type_amount_of_fire[0]
    amount = int(type_amount_of_fire[1])

    if water_lvl < amount:
        continue

    if type_fire == "High" and 81 <= amount <= 125:
        water_lvl -= amount
        effort_lvl += amount * 0.25
        fire_lvl += amount
    elif type_fire == "Medium" and 51 <= amount <= 80:
        water_lvl -= amount
        effort_lvl += amount * 0.25
        fire_lvl += amount
    elif type_fire == "Low" and 1 <= amount <= 50:
        water_lvl -= amount
        effort_lvl += amount * 0.25
        fire_lvl += amount
    else:
        continue
    print(f" - {amount}")

print(f"Effort: {effort_lvl:.2f}")
print(f"Total Fire: {fire_lvl}")
