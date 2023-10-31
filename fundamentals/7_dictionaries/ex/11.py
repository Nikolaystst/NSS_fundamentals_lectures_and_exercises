nss_dict = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        side, user = command.split(" | ")
        flag = False
        for key, val in nss_dict.items():
            if user in val:
                flag = True
                continue
        if side not in nss_dict.keys() and not flag:
            nss_dict[side] = [user]
        elif side in nss_dict.keys() and not flag:
            nss_dict[side].append(user)
    elif "->" in command:
        user, side = command.split(" -> ")
        for key, val in nss_dict.items():
            if user in val:
                nss_dict[key].remove(user)
                break
        if side not in nss_dict.keys():
            nss_dict[side] = [user]
        else:
            nss_dict[side].append(user)
        print(f"{user} joins the {side} side!")

for key, val in nss_dict.items():
    if len(val) > 0:
        print(f"Side: {key}, Members: {len(val)}")
        for i in val:
            print(f"! {i}")
