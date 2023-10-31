def dict_count(word, dict):
    for st in word:
        if st == " ":
            continue
        elif st not in dict:
            dict[st] = 0
        dict[st] += 1
    return dict


def printint(dict):
    for key, val in dict.items():
        print(f"{key} -> {val}")


word = input()
nss_dict = {}
dict_count(word, nss_dict)
printint(nss_dict)
