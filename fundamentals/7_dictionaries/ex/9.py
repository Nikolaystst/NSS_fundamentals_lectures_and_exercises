num = int(input())
nss_dict = {}

for _ in range(num):
    name = input()
    grade = float(input())
    if name not in nss_dict:
        nss_dict[name] = [grade]
    else:
        nss_dict[name].append(grade)

for name, grades in nss_dict.items():
    if sum(nss_dict[name]) / len(nss_dict[name]) >= 4.5:
        print(f"{name} -> {sum(nss_dict[name]) / len(nss_dict[name]):.2f}")
