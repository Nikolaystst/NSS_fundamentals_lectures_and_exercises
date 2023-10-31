nss_dict = {}

while True:
    command = input()
    if command == "statistics":
        break

    key, value = command.split(": ")

    if key not in nss_dict:
        nss_dict[key] = 0
    nss_dict[key] += int(value)


print("Products in stock:")
for key in nss_dict.keys():
    print(f"- {key}: {nss_dict[key]}")
print(f"Total Products: {len(nss_dict.keys())}")
print(f"Total Quantity: {sum(nss_dict.values())}")
