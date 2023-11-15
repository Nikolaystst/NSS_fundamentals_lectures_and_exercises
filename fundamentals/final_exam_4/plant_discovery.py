n = int(input())
nss_dict = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    nss_dict[plant] = {"rarity": rarity, "rate": []}

while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.split(":")
    to_do = command[0]
    command = command[1].strip(" ").split(" - ")
    if to_do == "Rate":
        plant = command[0]
        if plant in nss_dict.keys():
            rate = int(command[1])
            nss_dict[plant]["rate"].append(rate)
        else:
            print("error")
    elif to_do == "Update":
        plant = command[0]
        if plant in nss_dict.keys():
            new_rarity = command[1]
            nss_dict[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif to_do == "Reset":
        plant = command[0]
        if plant not in nss_dict.keys():
            print("error")
        else:
            nss_dict[plant]["rate"] = []

print("Plants for the exhibition:")
for plants, keys in nss_dict.items():
    if len(keys['rate']) == 0:
        print(f"- {plants}; Rarity: {keys['rarity']}; Rating: 0.00")
    else:
        print(f"- {plants}; Rarity: {keys['rarity']}; Rating: {sum(keys['rate']) / len(keys['rate']):.2f}")