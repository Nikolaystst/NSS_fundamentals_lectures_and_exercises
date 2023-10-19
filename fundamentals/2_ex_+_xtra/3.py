chars = int(input())
max_persons = int(input())

if chars % max_persons != 0:
    print(int(chars // max_persons) + 1)
else:
    print(int(chars / max_persons))
