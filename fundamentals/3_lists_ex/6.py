my_list = input().split()
num = int(input())
my_list = [int(x) for x in my_list]
min_num = 0

for i in range(num):
    min_num = min(my_list)
    my_list.remove(min_num)

my_list = [str(x) for x in my_list]
print(", ".join(my_list))
