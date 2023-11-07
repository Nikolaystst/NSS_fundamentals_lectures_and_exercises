import re

nss_patern = r"\b(?<![.-])[A-Za-z0-9.%+-]+@[A-Za-z0-9*][A-Za-z0-9._%+-]*\.[A-Za-z]{2,}(?:\.[A-Za-z]+)*\b"
word = input().split()
for email in word:
    final_end = re.findall(nss_patern, email)
    if final_end != []:
        print("".join(final_end))
