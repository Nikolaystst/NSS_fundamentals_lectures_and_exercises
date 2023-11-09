nss_dict = {}
n = int(input())

for _ in range(n):
    text = input().split("|")
    car = text[0]
    millage = int(text[1])
    fuel = int(text[2])
    nss_dict[car] = [millage, fuel]

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")
    to_do = command[0]

    if to_do == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > nss_dict[car][1]:
            print("Not enough fuel to make that ride")
        elif fuel <= nss_dict[car][1]:
            nss_dict[car][0] += distance
            nss_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if nss_dict[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del nss_dict[car]

    elif to_do == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if (nss_dict[car][1] + fuel) > 75:
            print(f"{car} refueled with {75 - nss_dict[car][1]} liters")
            nss_dict[car][1] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
            nss_dict[car][1] += fuel
    elif to_do == "Revert":
        car = command[1]
        distance = int(command[2])
        if (nss_dict[car][0] - distance) < 10000:
            nss_dict[car][0] = 10000
        else:
            nss_dict[car][0] -= distance
            print(f"{car} mileage decreased by {distance} kilometers")

for cars, km_fuel in nss_dict.items():
    print(f"{cars} -> Mileage: {km_fuel[0]} kms, Fuel in the tank: {km_fuel[1]} lt.")
