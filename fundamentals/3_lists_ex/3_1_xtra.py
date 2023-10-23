my_list = input().split(", ")
my_list = [int(num) for num in my_list]
my_list = [num for num in my_list if num != 0] + [num for num in my_list if num == 0]

print(my_list)
