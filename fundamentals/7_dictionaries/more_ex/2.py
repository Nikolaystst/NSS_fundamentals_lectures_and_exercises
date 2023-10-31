nss_dict = {}
algo_dict = {}
maxed_points = {}

while True:
    command = input()
    if command == "no more time":
        break
    name, exam, points = command.split(" -> ")

    if name not in nss_dict:
        nss_dict[name] = {exam: int(points)}
    elif exam not in nss_dict[name]:
        nss_dict[name][exam] = int(points)
    elif exam in nss_dict[name] and int(points) > nss_dict[name][exam]:
        nss_dict[name][exam] = int(points)

    if exam not in algo_dict:
        algo_dict[exam] = {name: int(points)}
    elif name not in algo_dict[exam]:
        algo_dict[exam][name] = int(points)
    elif name in algo_dict[exam] and int(points) > algo_dict[exam][name]:
        algo_dict[exam][name] = int(points)

for exam, name_points in algo_dict.items():
    print(f"{exam}: {len(name_points)} participants")
    counter = 0
    for name, points in sorted(name_points.items(), key=lambda x: (-x[1], x[0])):
        print(f"{counter + 1}. {name} <::> {points}")
        counter += 1
print("Individual standings:")
for key, val in nss_dict.items():
    maxed_points[key] = sum(val.values())
counter = 1
for name, points in sorted(maxed_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{counter}. {name} -> {points}")
    counter += 1
