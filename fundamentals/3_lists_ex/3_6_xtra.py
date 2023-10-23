list_of_nums = input().split()
list_of_nums = [int(x) for x in list_of_nums]
command = "o"

while command[0] != "end":
    command = input().split()
    if command[0] == "exchange":
        idx = int(command[1])
        if idx < 0 or idx >= len(list_of_nums):
            print("Invalid index")
        else:
            list_of_nums = list_of_nums[idx + 1:] + list_of_nums[:idx + 1]
    elif command[0] == "max":
        if command[1] == "even":
            elements = [x for x in list_of_nums if x % 2 == 0]
        else:
            elements = [x for x in list_of_nums if x % 2 == 1]
        if elements:
            print(len(list_of_nums) - list_of_nums[::-1].index(max(elements)) - 1)
        else:
            print("No matches")
    elif command[0] == "min":
        if command[1] == "even":
            elements = [x for x in list_of_nums if x % 2 == 0]
        else:
            elements = [x for x in list_of_nums if x % 2 == 1]
        if elements:
            print(len(list_of_nums) - list_of_nums[::-1].index(min(elements)) - 1)
        else:
            print("No matches")
    elif command[0] == "first":
        if command[2] == "even":
            elements = [x for x in list_of_nums if x % 2 == 0]
        else:
            elements = [x for x in list_of_nums if x % 2 == 1]
        if int(command[1]) > len(list_of_nums):
            print("Invalid count")
        else:
            print(elements[:int(command[1])])
    elif command[0] == "last":
        count = int(command[1])
        if command[2] == "even":
            elements = [x for x in list_of_nums if x % 2 == 0]
        else:
            elements = [x for x in list_of_nums if x % 2 == 1]
        if count > len(list_of_nums):
            print("Invalid count")
        else:
            print(elements[-count:])


print(list_of_nums)
