lines = int(input())
full_tank = 0

for i in range(lines):
    liters = int(input())
    full_tank += liters
    if full_tank > 255:
        print("Insufficient capacity!")
        full_tank -= liters

print(full_tank)
