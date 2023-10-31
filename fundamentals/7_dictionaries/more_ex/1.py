exams_pass_dict = {}
nss_dict = {}
maxed_points = {}

while True:
    command = input()
    if command == "end of contests":
        break
    command = command.split(":")
    exams_pass_dict[command[0]] = command[1]

while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    if contest in exams_pass_dict.keys():
        if password == exams_pass_dict[contest]:
            if username not in nss_dict:
                nss_dict[username] = {contest: int(points)}
            elif username in nss_dict:
                if contest not in nss_dict[username]:
                    nss_dict[username][contest] = int(points)
                elif nss_dict[username][contest] < int(points):
                    nss_dict[username][contest] = int(points)

for name, poits in nss_dict.items():
    maxed_points[name] = sum(poits.values())

best_name, max_poits = max(maxed_points.items(), key=lambda x: x[1])

print(f"Best candidate is {best_name} with total {max_poits} points.")
print("Ranking:")
for name in sorted(nss_dict.keys()):
    print(name)
    for sub, points in sorted(nss_dict[name].items(), key=lambda x: (-x[1], x[0])):
        print(f"#  {sub} -> {points}")
