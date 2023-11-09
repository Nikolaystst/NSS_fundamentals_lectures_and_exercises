dict_made_by_lss = {}
counter = 0

while True:

    command = input()

    if command == "Stop":
        break

    command = command.split("-")
    do_it = command[0]
    guest = command[1]
    food = command[2]

    if do_it == "Like":
        if guest not in dict_made_by_lss.keys():
            dict_made_by_lss[guest] = []
        if food not in dict_made_by_lss[guest]:
            dict_made_by_lss[guest].append(food)

    elif do_it == "Dislike":
        if guest not in dict_made_by_lss.keys():
            print(f"{guest} is not at the party.")
        elif food not in dict_made_by_lss[guest]:
            print(f"{guest} doesn't have the {food} in his/her collection.")
        else:
            dict_made_by_lss[guest].remove(food)
            print(f"{guest} doesn't like the {food}.")
            counter += 1

for key_1, val_1 in dict_made_by_lss.items():
    print(f"{key_1}: {', '.join(val_1)}")
print(f"Unliked meals: {counter}")
