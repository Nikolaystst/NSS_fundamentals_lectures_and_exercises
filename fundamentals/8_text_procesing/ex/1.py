names = input().split(", ")
valid_names = []
flag = False

for name in names:
    if 3 <= len(name) <= 16:
        flag = False
        for i in name:
            if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or ord(i) == 95 or ord(i) == 45:
                pass
            else:
                flag = True
        if not flag:
            valid_names.append(name)

print("\n".join(valid_names))
