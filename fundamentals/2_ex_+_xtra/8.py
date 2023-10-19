group_size = int(input())
days = int(input())
all_coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
    all_coins = int(all_coins + 50) - (group_size * 2)
    if i % 3 == 0:
        all_coins -= group_size * 3
    if i % 5 == 0:
        all_coins += group_size * 20
        if i % 3 == 0:
            all_coins -= group_size * 2

print(f"{group_size} companions received {int(all_coins / group_size)} coins each.")
