# bread 10 butter 4 sugar 9 jam 12
word = input().split()
nss_dict = {}

for idx in range(0, len(word), 2):
    key = word[idx]
    value = int(word[idx + 1])
    nss_dict[key] = value

print(nss_dict)
