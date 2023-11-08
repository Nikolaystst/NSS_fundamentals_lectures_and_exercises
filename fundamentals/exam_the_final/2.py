import re

nss_regex = r"(@|#)+([a-z]{3,})(@|#)+([^A-Za-z0-9])*(\/+)(\d+)(\/+)"
word = input()
final = re.finditer(nss_regex, word)

for one in final:
    print(f"You found {one.group(6)} {one.group(2)} eggs!")
