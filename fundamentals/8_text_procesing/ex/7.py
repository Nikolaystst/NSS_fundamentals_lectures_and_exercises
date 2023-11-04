text = input()
new_text = ""
power = 0

for i in range(len(text)):

    if power > 0 and text[i] != ">":
        power -= 1
    elif text[i] == ">":
        new_text += text[i]
        power += int(text[i + 1])
    else:
        new_text += text[i]

print(new_text)
