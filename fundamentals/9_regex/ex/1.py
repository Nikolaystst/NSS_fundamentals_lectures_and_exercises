import re

nss_lst = []
nss_patern = r"\d+"
while True:
    word = input()
    if not word:
        break
    searched = re.findall(nss_patern, word)
    nss_lst.extend(searched)

print(" ".join(nss_lst))
