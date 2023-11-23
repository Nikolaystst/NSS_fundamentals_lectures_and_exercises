import re


nss_pattern = r"(\*\*|\:\:)([A-Z][a-z]{2,})(\1)"
digit_patern = r"\d"
text = input()
lucky = 1
regex = re.compile(nss_pattern)
digits = re.findall(digit_patern, text)
digits = [int(x) for x in digits]
for x in digits:
    lucky *= x
words = re.finditer(regex, text)
count = 0
for me in words:
    if me.group(2):
        count += 1
nss_lst = []
words = re.finditer(regex, text)
for word in words:
    final_num = 0
    for x in word.group(2):
        final_num += ord(x)
        if final_num > lucky:
            nss_lst.append(word.group(1) + word.group(2) + word.group(3))
            break

print(f"Cool threshold: {lucky}")
print(f"{count} emojis found in the text. The cool ones are:")
for b in nss_lst:
    print(b)
