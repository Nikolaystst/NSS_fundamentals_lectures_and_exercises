number = int(input())
new_num = 0

for i in range(1, number + 1):
    special_num = False

    if len(str(i)) == 2:
        new_num = (i // 10) + (i % 10)
    else:
        new_num = i

    if new_num == 5 or new_num == 7 or new_num == 11:
        special_num = True

    print(f"{i} -> {special_num}")
