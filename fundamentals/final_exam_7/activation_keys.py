key = input()

while True:
    command = input()
    if command == "Generate":
        break
    command = command.split(">>>")
    if command[0] == "Contains":
        sub_str = command[1]
        if sub_str in key:
            print(f"{key} contains {sub_str}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        to_do = command[1]
        start_ind = int(command[2])
        end_ind = int(command[3])
        if to_do == "Upper":
            key = key[:start_ind] + key[start_ind:end_ind].upper() + key[end_ind:]
        elif to_do == "Lower":
            key = key[:start_ind] + key[start_ind:end_ind].lower() + key[end_ind:]
        print(key)
    elif command[0] == "Slice":
        start_ind = int(command[1])
        end_ind = int(command[2])
        key = key[:start_ind] + key[end_ind:]
        print(key)

print(f"Your activation key is: {key}")
