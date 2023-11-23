nss_dict = {}
num = int(input())

for _ in range(num):
    word = input().split(" ")
    nss_dict[word[0]] = {"HP": int(word[1]), "MP": int(word[2])}

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" - ")
    to_do = command[0]
    hero_name = command[1]
    if to_do == "CastSpell":
        mp_need = int(command[2])
        spell_name = command[3]
        if nss_dict[hero_name]["MP"] - mp_need < 0:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            nss_dict[hero_name]["MP"] -= mp_need
            print(f"{hero_name} has successfully cast {spell_name} and now has {nss_dict[hero_name]['MP']} MP!")
    elif to_do == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if nss_dict[hero_name]["HP"] - damage <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
            del nss_dict[hero_name]
        else:
            nss_dict[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {nss_dict[hero_name]['HP']} HP left!")
    elif to_do == "Recharge":
        amount = int(command[2])
        if nss_dict[hero_name]['MP'] + amount > 200:
            print(f"{hero_name} recharged for {200 - nss_dict[hero_name]['MP']} MP!")
            nss_dict[hero_name]['MP'] = 200
        else:
            nss_dict[hero_name]['MP'] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif to_do == "Heal":
        amount = int(command[2])
        if nss_dict[hero_name]['HP'] + amount > 100:
            print(f"{hero_name} healed for {100 - nss_dict[hero_name]['HP']} HP!")
            nss_dict[hero_name]['HP'] = 100
        else:
            nss_dict[hero_name]['HP'] += amount
            print(f"{hero_name} healed for {amount} HP!")

for name, val in nss_dict.items():
    print(name)
    print(f"  HP: {nss_dict[name]['HP']}")
    print(f"  MP: {nss_dict[name]['MP']}")
