words = input().lower().split()
nss_dict = {}

for i in words:
    if i not in nss_dict.keys():
        nss_dict[i] = 0
    nss_dict[i] += 1

for key, val in nss_dict.items():
    if val % 2 != 0:
        print(key, end=" ")
