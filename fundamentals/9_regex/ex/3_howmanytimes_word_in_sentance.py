import re

word = input().lower()
one = re.findall(rf"{input().lower()}\b", word)
print(len(one))
