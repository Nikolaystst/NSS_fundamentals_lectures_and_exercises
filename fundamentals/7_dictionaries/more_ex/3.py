nss_dict = {}
flag_1 = False
flag_2 = False

while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:
        name, position, skill = command.split(" -> ")
        if name not in nss_dict:
            nss_dict[name] = {position: int(skill)}
        elif name in nss_dict.keys() and position not in nss_dict[name].keys():
            nss_dict[name][position] = int(skill)
        elif name in nss_dict.keys() and position in nss_dict[name].keys() and int(skill) > nss_dict[name][position]:
            nss_dict[name][position] = int(skill)

    elif " vs " in command:
        name, name_2 = command.split(" vs ")
        if name in nss_dict and name_2 in nss_dict:
            for key in nss_dict[name]:
                for key_2 in nss_dict[name_2]:
                    if key == key_2:
                        if nss_dict[name][key] > nss_dict[name_2][key_2]:
                            del nss_dict[name_2]
                        elif nss_dict[name][key] < nss_dict[name_2][key_2]:
                            del nss_dict[name]

nss_dict = dict(sorted(nss_dict.items(), key=lambda x: sum(x[1].values()), reverse=True))
# sortnah po sumata na valutata
for key, value in nss_dict.items():
    nss_dict[key] = dict(sorted(value.items(), key=lambda x: -x[1]))
#     sortnah po 2ri nai golqma value
for name, skill in nss_dict.items():
    print(f"{name}: {sum(skill.values())} skill")
    for position, skill_2 in skill.items():
        print(f"- {position} <::> {skill_2}")
