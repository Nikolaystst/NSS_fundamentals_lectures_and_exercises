lst_1 = input().split(", ")
lst_2 = input().split(", ")
lst_3 = []

for i in lst_1:
    for y in lst_2:
        if i in y and i not in lst_3:
            lst_3.append(i)

print(lst_3)
