nss_dict = {"shards": 0, "fragments": 0, "motes": 0}
flag = False

while not flag:
    command = input().split()
    for index in range(0, len(command), 2):
        val = command[index]
        key = command[index + 1].lower()
        if key not in nss_dict:
            nss_dict[key] = 0
        nss_dict[key] += int(val)
        if nss_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            nss_dict["shards"] -= 250
            flag = True
        elif nss_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            nss_dict["fragments"] -= 250
            flag = True
        elif nss_dict["motes"] >= 250:
            print("Dragonwrath obtained!")
            nss_dict["motes"] -= 250
            flag = True
        if flag:
            break

for key, val in nss_dict.items():
    print(f"{key}: {val}")
