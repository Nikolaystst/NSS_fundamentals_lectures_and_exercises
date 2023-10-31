nss_dict = {}
num = int(input())

for i in range(num):
    word = input()
    sinonym = input()
    if word not in nss_dict.keys():
        nss_dict[word] = []
    nss_dict[word].append(sinonym)

for key in nss_dict.keys():
    print(f"{key} - {', '.join(nss_dict[key])}")
