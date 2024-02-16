neighbourhood = [int(x) for x in input().split('@')]
current_loc = 0
total = 0

while True:
    command = input()

    if command == 'Love!':
        break

    jump = int(command.split()[1])

    current_loc += jump

    if current_loc >= len(neighbourhood):
        current_loc = 0

    if neighbourhood[current_loc] == 0:
        print(f"Place {current_loc} already had Valentine's day.")
    elif neighbourhood[current_loc] > 0:
        neighbourhood[current_loc] -= 2
        if neighbourhood[current_loc] == 0:
            print(f"Place {current_loc} has Valentine's day.")

print(f"Cupid's last position was {current_loc}.")

for i in neighbourhood:
    if i != 0:
        total += 1

if total == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {total} places.")
