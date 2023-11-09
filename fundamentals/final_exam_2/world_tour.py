travel_destination = input()

while True:
    command = input()
    if command == "Travel":
        break

    command = command.split(":")
    to_do = command[0]

    if to_do == "Add Stop":
        index = int(command[1])
        string_1 = command[2]
        if 0 <= index < len(travel_destination):
            travel_destination = travel_destination[:index] + string_1 + travel_destination[index:]
    elif to_do == "Remove Stop":
        index_start = int(command[1])
        index_end = int(command[2])
        if 0 <= index_start < len(travel_destination) and 0 <= index_end < len(travel_destination):
            travel_destination = travel_destination[:index_start] + travel_destination[index_end + 1:]
    elif to_do == "Switch":
        old_str = command[1]
        new_str = command[2]
        if old_str in travel_destination:
            travel_destination = travel_destination.replace(old_str, new_str)
    print(travel_destination)

print(f"Ready for world tour! Planned stops: {travel_destination}")
