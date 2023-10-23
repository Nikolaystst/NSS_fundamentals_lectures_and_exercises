word = input().split()
my_list = [int(x) for x in word]
opposite_list = [-x for x in my_list]
print(opposite_list)
