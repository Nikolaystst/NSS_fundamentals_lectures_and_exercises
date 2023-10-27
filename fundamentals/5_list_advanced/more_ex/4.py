rows = int(input())
my_list = []
counter = 0
counter_2 = 0
for i in range(rows):
    lines = input().split()
    lines = [int(x) for x in lines]
    my_list.append(lines)

for l in my_list:
    counter += l.count(0)

atacks = input().split()

for i in atacks:
    row, col = i.split("-")
    row = int(row)
    col = int(col)
    my_list[row][col] = my_list[row][col] - 1
    if my_list[row][col] == -1:
        my_list[row][col] = 0

for s in my_list:
    counter_2 += s.count(0)

print(counter_2 - counter)
