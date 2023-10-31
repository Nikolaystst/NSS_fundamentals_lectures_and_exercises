num = int(input())
nss_dict = {}

for _ in range(num):
    command = input().split()
    if command[0] == "register":
        owner = command[1]
        license_plate = command[2]
        if owner in nss_dict.keys():
            print(f"ERROR: already registered with plate number {nss_dict[owner]}")
        elif owner not in nss_dict.keys():
            nss_dict[owner] = license_plate
            print(f"{owner} registered {license_plate} successfully")
    elif command[0] == "unregister":
        owner = command[1]
        if owner not in nss_dict.keys():
            print(f"ERROR: user {owner} not found")
        elif owner in nss_dict.keys():
            print(f"{owner} unregistered successfully")
            del nss_dict[owner]

for key, val in nss_dict.items():
    print(f"{key} => {val}")
