my_list = input().split()
my_list_2 = []
shuffels = int(input())

for i in range(shuffels):
    for idx in range(int(len(my_list) / 2)):
        my_list_2.append(my_list[0])
        my_list_2.append(my_list[int((len(my_list) / 2))])
        my_list.pop(int((len(my_list) / 2)))
        my_list.pop(0)

    my_list = my_list_2
    my_list_2 = []

print(my_list)
