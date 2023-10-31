nss_dict = {}

while True:
    command = input()
    if command == "end":
        break
    key, value = command.split(" : ")
    if key not in nss_dict:
        nss_dict[key] = [value]
    else:
        nss_dict[key].append(value)

for key, val in nss_dict.items():
    print(f"{key}: {len(nss_dict[key])}")
    for i in val:
        print(f"-- {i}")
