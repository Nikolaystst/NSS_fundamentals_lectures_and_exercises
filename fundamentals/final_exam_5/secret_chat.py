word = input()

while True:
    command = input()
    if command == "Reveal":
        break

    command = command.split(":|:")

    to_do = command[0]
    if to_do == "InsertSpace":
        index = int(command[1])
        word = word[:index] + " " + word[index:]
        print(word)
    elif to_do == "Reverse":
        substr = command[1]
        if substr in word:
            word = word.replace(substr, "", 1)
            word = word + substr[::-1]
            print(word)
        else:
            print("error")
    elif to_do == "ChangeAll":
        old = command[1]
        new = command[2]
        word = word.replace(old, new)
        print(word)

print(f"You have a new text message: {word}")
