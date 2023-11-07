import re

total_cost = 0
furniture_list = []

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.search(r">>(\w+)<<([\d\.]+)!([\d]+)", line)
    # ([\d\.]+) matchva float ([\d]+)matchva integer
    if not match:
        continue

    furniture_name = match.group(1)
    price = float(match.group(2))
    quantity = int(match.group(3))
    cost = price * quantity

    furniture_list.append(furniture_name)
    total_cost += cost

print("Bought furniture:")
for furniture in furniture_list:
    print(furniture)

print(f"Total money spend: {total_cost:.2f}")
