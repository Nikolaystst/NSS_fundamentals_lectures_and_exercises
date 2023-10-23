my_list = input().split()
shuffle = int(input())

for i in range(shuffle):

    my_list_2 = []
    my_list_3 = []
    my_list_4 = []

    for i in range(int(len(my_list) / 2)):
        my_list_2.append(my_list[i])

    for i in range(int(len(my_list) / 2), len(my_list)):
        my_list_3.append(my_list[i])

    for i in range(len(my_list_2)):
        my_list_4.append(my_list_2[i])
        my_list_4.append(my_list_3[i])

    my_list = my_list_4

print(my_list)