lst = input().split(", ")
lst = [int(x) for x in lst]
lst_ind = [lst.index(x) for x in lst if x % 2 == 0]

print(lst_ind)
