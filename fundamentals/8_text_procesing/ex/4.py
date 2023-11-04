name = input()
word = []
for i in name:
    b = ord(i) + 3
    word.append(chr(b))
print("".join(word))