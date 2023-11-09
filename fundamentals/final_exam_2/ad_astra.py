import re

nss_pattern = r"(\||\#)([A-Za-z\s*]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1(\d+)\1"
word = input()
regex = re.compile(nss_pattern)
finded = re.finditer(regex, word)
total_cal = 0

for x in finded:
    total_cal += int(x.group(4))

print(f"You have food to last you for: {total_cal // 2000} days!")
finded = re.finditer(regex, word)
for x in finded:
    print(f"Item: {x.group(2)}, Best before: {x.group(3)}, Nutrition: {x.group(4)}")