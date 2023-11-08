nss_dict = {}
counter = 0
while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("-")
    to_do = command[0]
    guest = command[1]
    meal = command[2]
    if to_do == "Like":
        if guest not in nss_dict.keys():
            nss_dict[guest] = []
        if meal not in nss_dict[guest]:
            nss_dict[guest].append(meal)
    elif to_do == "Dislike":
        if guest not in nss_dict.keys():
            print(f"{guest} is not at the party.")
        elif meal not in nss_dict[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            nss_dict[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            counter += 1

for key, val in nss_dict.items():
    print(f"{key}: {', '.join(val)}")
print(f"Unliked meals: {counter}")
