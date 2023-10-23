my_list = input().split(", ")
beggars = int(input())

beggars_list = [0] * beggars

for i in range(len(my_list)):
    index = i % beggars
    num = int(my_list[i])
    beggars_list[index] += num

print(beggars_list)
