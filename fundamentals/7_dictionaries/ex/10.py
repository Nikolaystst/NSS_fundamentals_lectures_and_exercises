nss_dict = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, id = command.split(" -> ")
    if company_name not in nss_dict:
        nss_dict[company_name] = [id]
    elif id not in nss_dict[company_name]:
        nss_dict[company_name].append(id)

for key, val in nss_dict.items():
    print(f"{key}")
    for i in val:
        print(f"-- {i}")
