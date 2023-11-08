import re
count = input()
zdr_patern = r"(.+)>([0-9]{3})(\|)([a-z]{3})\3([A-Z]{3})\3([^<>]{3})<\1"
for i in range(int(count)):
    flag = False
    line = input()
    final = re.finditer(zdr_patern, line)
    if re.match(zdr_patern, line):
        flag = True
    if flag:
        for f in final:
            word = f.group(2) + f.group(4) + f.group(5) + f.group(6)
            print(f"Password: {word}")
    else:
        print("Try another password!")

