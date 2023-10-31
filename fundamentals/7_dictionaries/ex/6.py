nss_dict = {}

while True:
    command = input()
    if command == "buy":
        break
    key, price, quant = command.split()

    if key not in nss_dict:
        nss_dict[key] = [float(price)]
    nss_dict[key][0] = float(price)
    nss_dict[key].append(int(quant))

for key in nss_dict.keys():
    print(f"{key} -> {nss_dict[key][0] * sum(nss_dict[key][1:]):.2f}")


