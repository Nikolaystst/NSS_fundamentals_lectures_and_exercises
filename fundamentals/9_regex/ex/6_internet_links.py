import re

nss_pattern = r"www\.[a-zA-Z0-9\-]+\.[a-zA-Z\.]+"
while True:
    texting = input()
    if not texting:
        break
    final = re.finditer(nss_pattern, texting)
    for text in final:
        print(text.group())