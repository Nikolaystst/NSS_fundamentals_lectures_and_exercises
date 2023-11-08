nss_lst = input().split("||")
starting_fuel = int(input())
starting_amunition = int(input())

for i in nss_lst:

    if i == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    i = i.split()
    command = i[0]
    amount = int(i[1])

    if command == "Travel":
        if amount > starting_fuel:
            print("Mission failed.")
            break
        else:
            starting_fuel -= amount
            print(f"The spaceship travelled {amount} light-years.")

    elif command == "Enemy":
        if starting_amunition >= amount:
            starting_amunition -= amount
            print(f"An enemy with {amount} armour is defeated.")
        elif starting_amunition < amount and starting_fuel >= (2 * amount):
            starting_fuel -= (2 * amount)
            print(f"An enemy with {amount} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    elif command == "Repair":
        starting_fuel += amount
        starting_amunition += (2 * amount)
        print(f"Ammunitions added: {2 * amount}.")
        print(f"Fuel added: {amount}.")
