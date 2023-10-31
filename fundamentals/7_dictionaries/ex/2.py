nss_dict = {}

while True:
    key = input()
    if key == "stop":
        break
    val = int(input())
    if key not in nss_dict.keys():
        nss_dict[key] = 0
    nss_dict[key] += val

for key in nss_dict.keys():
    print(f"{key} -> {nss_dict[key]}")
