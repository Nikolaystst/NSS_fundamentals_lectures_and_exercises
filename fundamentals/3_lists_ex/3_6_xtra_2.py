def manipulate_lists(lst, cmd):
    if cmd[0] == "exchange":
        idx = int(cmd[1])
        if idx < 0 or idx >= len(lst):
            print("Invalid index")
        else:
            lst[:] = lst[idx + 1:] + lst[:idx + 1]
    elif cmd[0] == "max":
        if cmd[1] == "even":
            elements = [x for x in lst if x % 2 == 0]
        else:
            elements = [x for x in lst if x % 2 == 1]
        if elements:
            b = max(elements) - 1
            c = lst[::-1].index(max(elements)) - 1
            print(len(lst) - lst[::-1].index(max(elements)) - 1)
        else:
            print("No matches")
    elif cmd[0] == "min":
        if cmd[1] == "even":
            elements = [x for x in lst if x % 2 == 0]
        else:
            elements = [x for x in lst if x % 2 == 1]
        if elements:
            print(len(lst) - lst[::-1].index(min(elements)) - 1)
        else:
            print("No matches")
    elif cmd[0] == "first":
        count = int(cmd[1])
        if cmd[2] == "even":
            elements = [x for x in lst if x % 2 == 0]
        else:
            elements = [x for x in lst if x % 2 == 1]
        if count > len(lst):
            print("Invalid count")
        else:
            print(elements[:count])
    elif cmd[0] == "last":
        count = int(cmd[1])
        if cmd[2] == "even":
            elements = [x for x in lst if x % 2 == 0]
        else:
            elements = [x for x in lst if x % 2 == 1]
        if count > len(lst):
            print("Invalid count")
        else:
            print(elements[-count:])
    return lst


lst = list(map(int, input().split()))
cmd = input().split()
while cmd[0] != "end":
    lst = manipulate_lists(lst, cmd)
    cmd = input().split()

print(lst)
