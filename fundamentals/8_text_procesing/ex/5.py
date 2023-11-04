code = input()

for i in range(len(code)):
    if code[i] == ":":
        print(f":{code[i + 1]}")
