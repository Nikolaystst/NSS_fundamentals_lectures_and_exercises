word = list(input())
symbols = []

for i in range(1, len(word)):
    if word[i] == word[i - 1]:
        continue
    else:
        symbols.append(word[i - 1])

if len(symbols) == 0:
    symbols.append(word[0])
elif word[len(word) - 1] != symbols[len(symbols) - 1]:
    symbols.append(word[len(word) - 1])

print("".join(symbols))
