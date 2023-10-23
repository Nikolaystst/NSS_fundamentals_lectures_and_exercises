events = input().split("|")
initial_energy = 100
initial_coins = 100
flag = False

for i in events:

    event_or_ingredient = i.split("-")[0]
    energy_or_coin = int(i.split("-")[1])

    if event_or_ingredient == "rest":
        initial_energy += energy_or_coin
        if initial_energy >= 100:
            print(f"You gained {energy_or_coin - (initial_energy - 100)} energy.")
        else:
            print(f"You gained {energy_or_coin} energy.")
        if initial_energy > 100:
            initial_energy = 100
        print(f"Current energy: {initial_energy}.")

    elif event_or_ingredient == "order":
        initial_coins += energy_or_coin
        initial_energy -= 30
        if initial_energy >= 0:
            print(f"You earned {energy_or_coin} coins.")
        else:
            initial_energy += 80
            initial_coins -= energy_or_coin
            print("You had to rest!")

    else:
        initial_coins -= energy_or_coin
        if initial_coins >= 0:
            print(f"You bought {event_or_ingredient}.")
        else:
            initial_coins += energy_or_coin
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            flag = True
            break

if not flag:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
else:
    pass
