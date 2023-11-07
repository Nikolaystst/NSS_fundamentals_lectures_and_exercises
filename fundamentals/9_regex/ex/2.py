import re

nss_lst = []
nss_patern = r"\b_{1}([a-zA-Z0-9]*\b)"
word = input()
final = re.finditer(nss_patern, word)
binal = re.search(nss_patern, word)
for one in final:
    nss_lst.append(one.group(1))
print(",".join(nss_lst))

