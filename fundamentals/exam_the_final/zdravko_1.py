word = input()

while True:
    command = input()
    if command == "Abracadabra":
        break
    command = command.split()

    if command[0] == "Abjuration":
        word = word.upper()
        print(word)
    elif command[0] == "Necromancy":
        word = word.lower()
        print(word)
    elif command[0] == "Illusion":
        n = int(command[1])
        char = command[2]
        if -1 < n < len(word):
            word = word[:n] + char + word[n + 1:]
            print("Done")
        else:
            print("The spell was too weak")
    elif command[0] == "Divination":
        sub_1 = command[1]
        sub_2 = command[2]
        if sub_1 in word:
            word = word.replace(sub_1, sub_2)
            print(word)
    elif command[0] == "Alteration":
        sub_3 = command[1]
        if sub_3 in word:
            word = word.replace(sub_3, "")
            print(word)
    else:
        print("The spell did not work!")
