my_dict = {}
zdr_lst = {}
while True:
    command = input()
    if command == "EndDay":
        break

    command, command_2 = command.split(": ")
    if command == "Add":
        command_2 = command_2.split("-")
        name = command_2[0]
        needed_food = int(command_2[1])
        area = command_2[2]
        if name not in my_dict.keys():
            my_dict[name] = {"food": needed_food, "area": area}
        elif name in my_dict.keys():
            my_dict[name]["food"] += needed_food
    elif command == "Feed":
        command_2 = command_2.split("-")
        name = command_2[0]
        food = int(command_2[1])
        if name in my_dict.keys():
            my_dict[name]["food"] -= food
            if my_dict[name]["food"] <= 0:
                print(f"{name} was successfully fed")
                del my_dict[name]
print("Animals:")
for names, vals in my_dict.items():
    print(f" {names} -> {vals['food']}g")
    if vals['area'] not in zdr_lst:
        zdr_lst[vals['area']] = 1
    elif vals['area'] in zdr_lst:
        zdr_lst[vals['area']] += 1
print("Areas with hungry animals:")
for k, v in zdr_lst.items():
    print(f' {k}: {v}')
