rows = int(input())
counter_1 = 0
counter_2 = 0
flag = False

for i in range(rows):
    char = input()

    if "(" in char:
        counter_1 += 1
    elif ")" in char:
        counter_2 += 1

    if counter_2 == 1 and counter_1 == 0:
        flag = True

    if counter_1 == 2 or counter_2 == 2:
        flag = True
        counter_1 = 0
        counter_2 = 0

    if counter_1 == 1 and counter_2 == 1:
        counter_1 = 0
        counter_2 = 0

if counter_1 != counter_2:
    flag = True

if flag:
    print("UNBALANCED")
else:
    print("BALANCED")
