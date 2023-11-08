password_ls = input()
count_up = 0
count_down = 0
count_digit = 0

while True:
    command = input()
    if command == "Complete":
        break
    command = command.split()

    if command[0] == "Make":
        up_down = command[1]
        index = int(command[2])
        if up_down == "Upper":
            password_ls = password_ls[:index] + password_ls[index].upper() + password_ls[index + 1:]
            print(password_ls)
        elif up_down == "Lower":
            password_ls = password_ls[:index] + password_ls[index].lower() + password_ls[index + 1:]
            print(password_ls)
    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]
        if -1 < index < len(password_ls) + 1:
            password_ls = password_ls[:index] + char + password_ls[index:]
            print(password_ls)
    elif command[0] == "Replace":
        char = command[1]
        val = int(command[2])
        if char in password_ls:
            replacement = ord(char)
            replacement += val
            replacement = chr(replacement)
            password_ls = password_ls.replace(char, replacement)
            print(password_ls)
    elif command[0] == "Validation":
        if len(password_ls) < 8:
            print("Password must be at least 8 characters long!")
        for x in password_ls:
            if x.isalnum() or x == "_":
                continue
            else:
                print("Password must consist only of letters, digits and _!")
                break
        for b in password_ls:
            if b.isupper():
                count_up += 1
            elif b.islower():
                count_down += 1
            elif b.isdigit():
                count_digit += 1
        if count_up == 0:
            print("Password must consist at least one uppercase letter!")
        if count_down == 0:
            print("Password must consist at least one lowercase letter!")
        if count_digit == 0:
            print("Password must consist at least one digit!")

