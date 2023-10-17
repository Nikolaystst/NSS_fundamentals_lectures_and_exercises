quantity = int(input())
days = int(input())
total_cost = 0
total_spirit = 0

ornament_price = 2
ornament_points = 5
skirt_price = 5
skirt_points = 3
gerland_price = 3
gerland_points = 10
lights_price = 15
lights_points = 17

if days % 10 == 0:
    total_spirit -= 30

for i in range(1, days + 1):
    if i % 2 == 0:
        total_cost += ornament_price * quantity
        total_spirit += ornament_points
    if i % 3 == 0:
        total_cost += (skirt_price + gerland_price) * quantity
        total_spirit += skirt_points + gerland_points
    if i % 5 == 0:
        total_cost += lights_price * quantity
        total_spirit += lights_points
    if i % 5 == 0 and i % 3 == 0:
        total_spirit += 30
    if i % 10 == 0:
        total_spirit -= 20
        total_cost += skirt_price + gerland_price + lights_price
    if i % 11 == 0:
        quantity += 2

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

