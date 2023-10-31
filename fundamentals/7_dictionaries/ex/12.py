nss_dict_sub_times = {}
nss_dict_names_points = {}

while True:
    command = input()
    if command == "exam finished":
        break
    splited = command.split("-")
    if len(splited) > 2:
        name, sub, poits = splited[0], splited[1], int(splited[2])
        if sub not in nss_dict_sub_times:
            nss_dict_sub_times[sub] = 0
        nss_dict_sub_times[sub] += 1
        if name not in nss_dict_names_points:
            nss_dict_names_points[name] = poits
        elif name in nss_dict_names_points:
            if nss_dict_names_points[name] < poits:
                nss_dict_names_points[name] = poits
    elif len(splited) == 2:
        name_to_ban = splited[0]
        del nss_dict_names_points[name_to_ban]

print("Results:")
for key, val in nss_dict_names_points.items():
    print(f"{key} | {val}")
print("Submissions:")
for key, val in nss_dict_sub_times.items():
    print(f"{key} - {val}")
