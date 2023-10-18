year = int(input())

while True:
    year += 1
    my_set = set(str(year))
    if len(my_set) == len(str(year)):
        break

print(year)
