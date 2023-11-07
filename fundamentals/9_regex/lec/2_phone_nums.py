import re

nss_pattern = r"\+359\ 2\ \d{3}\ \d{4}\b|\+359\-2\-\d{3}\-\d{4}\b"
word = input()
output = re.findall(nss_pattern, word)

print(", ".join(output))
