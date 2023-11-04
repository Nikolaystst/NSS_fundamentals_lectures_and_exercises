word = input()
digits = []
alphabet = []
symbols = []

for i in word:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        alphabet.append(i)
    else:
        symbols.append(i)

print("".join(digits))
print("".join(alphabet))
print("".join(symbols))
