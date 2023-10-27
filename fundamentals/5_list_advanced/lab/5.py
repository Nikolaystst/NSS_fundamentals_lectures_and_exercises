def lenght_alphabetic_sorting(lst):
    lst = sorted(lst, key=lambda x: (-len(x), x))
    return lst


names = input().split(", ")
print(lenght_alphabetic_sorting(names))
