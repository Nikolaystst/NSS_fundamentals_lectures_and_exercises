word = input()

while True:
    command = input()
    if command == "Done":
        break

    command = command.split(" ")
    to_do = command[0]

    if to_do == "TakeOdd":
        word_2 = ""
        count = 1
        for x in word:
            if count % 2 == 0:
                word_2 += x
            count += 1
        word = word_2
        print(word)
    elif to_do == "Cut":
        index = int(command[1])
        lenght = int(command[2])
        word = word[:index] + word[index + lenght:]
        print(word)
    elif to_do == "Substitute":
        old_str = command[1]
        new_str = command[2]
        if old_str in word:
            word = word.replace(old_str, new_str)
            print(word)
        else:
            print("Nothing to replace!")

print(f"Your password is: {word}")
