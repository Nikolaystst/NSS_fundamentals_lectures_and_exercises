while True:
    word = input()
    if word == "End":
        break
    elif word == "SoftUni":
        continue
    for i in word:
        print(i * 2, end="")
    print()