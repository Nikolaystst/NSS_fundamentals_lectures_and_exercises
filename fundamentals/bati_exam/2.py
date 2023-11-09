import re

count = int(input())
lss_pattern = r"(\!)([A-Z*1][a-z]{2,})(\1)(\:)(\[)([a-zA-Z]{8,})(\])"
final = []

for i in range(count):
    word = input()
    res = re.search(lss_pattern, word)
    try:
        command = res.group(2)
        final_word = res.group(6)

    except AttributeError:
        final.append("The message is invalid")
        continue

    res = f"{command}:"
    for symb in final_word:
        res += f" {ord(symb)}"
    final.append(res)

print("\n".join(final))

