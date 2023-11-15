import re

nss_patern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
word = input()
final = re.finditer(nss_patern, word)
points = 0
txt = []
for h in final:
    txt.append(h.group(2))
    points += len(h.group(2))

print(f"Destinations: {', '.join(txt)}")
print(f"Travel Points: {points}")
