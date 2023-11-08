import re

nss_pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"
rounds = int(input())

for _ in range(rounds):
    barcode = input()
    if re.match(nss_pattern, barcode):
        digits = ""
        for i in barcode:
            if i.isdigit():
                digits += i
        if digits == "":
            print("Product group: 00")
        else:
            print(f"Product group: {digits}")
    else:
        print("Invalid barcode")
