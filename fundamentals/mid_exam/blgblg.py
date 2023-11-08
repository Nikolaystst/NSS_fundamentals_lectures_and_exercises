word = input().split("|")
word = [int(x) for x in word]
points = 0
while True:
    command = input()
    if command == "Game over":
        break

    command = command.split("@")
    if command[0] == "Shoot Left":
        index = int(command[1])
        lght = int(command[2])
        if 0 > index or index >= len(word):
            continue
        elif index - lght < 0:
            lght = lght % len(word)
            new_idx = len(word) - index - lght
        else:
            new_idx = index - lght
        if word[new_idx] < 5:
            points += word[new_idx]
            word[new_idx] = 0
        else:
            word[new_idx] -= 5
            points += 5

    elif command[0] == "Shoot Right":
        index = int(command[1])
        lght = int(command[2])
        if 0 > index or index >= len(word):
            continue
        elif index + lght >= len(word):
            new_idx = (index + lght) % len(word)
        else:
            new_idx = index + lght
        if word[new_idx] < 5:
            points += word[new_idx]
            word[new_idx] = 0
        else:
            word[new_idx] -= 5
            points += 5

    elif command[0] == "Reverse":
        word.reverse()

word = [str(x) for x in word]
print(" - ".join(word))
print(f"John finished the archery tournament with {points} points!")
