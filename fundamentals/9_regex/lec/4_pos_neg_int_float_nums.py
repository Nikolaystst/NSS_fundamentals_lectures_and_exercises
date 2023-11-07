import re

nss_pattern = r"(^|(?<=\s))-?(0|[1-9][0-9]*)(\.\d*)?($|(?=\s))"
word = input()
if_match = re.finditer(nss_pattern, word)
for match in if_match:
    print(match.group())
