numbers = input().split()
final = ""
my_list = []
k = int(input())
idx = 0

while len(numbers) > 0:
    idx = (idx + k - 1) % len(numbers)
    # ^^^^^^^^^^ klu4yt kym istinata
    final += f"{numbers[idx]},"
    numbers.pop(idx)

my_list = final.split(",")
my_list.pop(-1)
print("[", end="")
for i in range(len(my_list)):
    if i == len(my_list) - 1:
        print(my_list[i], end="]")
    else:
        print(my_list[i], end=",")
