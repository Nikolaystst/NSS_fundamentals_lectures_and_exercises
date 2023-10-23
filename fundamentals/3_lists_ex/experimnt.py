my_list = input().split()
my_list_2 = []

for i in my_list:
    task = i.split("-")
    my_list_2.append([task[0], task[1]])

sorted_list = [x[1] for x in sorted(my_list_2)]
print(sorted_list)
