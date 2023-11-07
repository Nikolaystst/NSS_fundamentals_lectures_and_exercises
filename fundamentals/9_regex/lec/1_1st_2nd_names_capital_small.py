import re

regex = r"\b[A-Z][a-z]+\ [A-Z][a-z]+\b"
text = input()
output = re.findall(regex, text)

print(" ".join(output))
