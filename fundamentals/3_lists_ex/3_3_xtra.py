# 29 13 9 0 13 0 21 0 14 82 12
my_list = (input().split())
my_list = [int(x) for x in my_list]
b = int(len(my_list) / 2)
my_list_2 = my_list[:b]
my_list_3 = my_list[b + 1:]
my_list_3.reverse()
a = 0
b = 0

for index in my_list_2:
    if index == 0:
        a *= 0.8
    else:
        a += index

for index_2 in my_list_3:
    if index_2 == 0:
        b *= 0.8
    else:
        b += index_2

if a < b:
    print(f"The winner is left with total time: {a:.1f}")
else:
    print(f"The winner is right with total time: {b:.1f}")
