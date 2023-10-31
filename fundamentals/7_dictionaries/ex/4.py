nss_dict = {}
word = ""

while True:
    word = input()
    if len(word) <= 2:
        break
    key, val = word.split("-")
    nss_dict[key] = val

word = int(word)

for i in range(word):
    searched_name = input()
    if searched_name in nss_dict.keys():
        print(f"{searched_name} -> {nss_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
