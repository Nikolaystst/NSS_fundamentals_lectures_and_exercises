word = input().split()

while True:
    filtered = input().split()
    if filtered[0] == "No" and filtered[1] == "Money":
        break
    elif filtered[0] == "OutOfStock":
        for i in range(len(word)):
            if word[i] == filtered[1]:
                word[i] = "None"
    elif filtered[0] == "Required":
        if 0 <= int(filtered[2]) < len(word):
            word[int(filtered[2])] = filtered[1]
        else:
            continue
    else:
        word[-1] = filtered[1]

for i in word:
    if i == "None":
        continue
    else:
        print(i, end=" ")
