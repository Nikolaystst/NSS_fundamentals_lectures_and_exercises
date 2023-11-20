import re

nss_pattern = r"(\@|\#)([A-Za-z]{3,})\1(\@|\#)([A-Za-z]{3,})\1"
word = input()
nss_lst = []
nss_lst_2 = []
finded = re.findall(nss_pattern, word)
for word in finded:
    nss_lst.append(word[1])
    nss_lst.append(word[3])
if len(nss_lst) == 0:
    print("No word pairs found!")
else:
    print(f"{int(len(nss_lst) / 2)} word pairs found!")

for n in range(0, len(nss_lst), 2):
    if nss_lst[n] == nss_lst[n + 1][::-1]:
        nss_lst_2.append(f"{nss_lst[n]} <=> {nss_lst[n + 1]}")

if nss_lst_2:
    print("The mirror words are:")
    print(", ".join(nss_lst_2))
else:
    print("No mirror words!")
