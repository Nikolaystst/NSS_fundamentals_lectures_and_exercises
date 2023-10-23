b = 0
my_list = input().split()
word = list(input())
output = ""
a = 0
c = 0

for x in my_list:
    for i in x:
        b += int(i)
    my_list[a] = f"{b}"
    b = 0
    a += 1

for y in range(len(my_list)):
    c = int(my_list[y]) % len(word)
    output += word[c]
    word.pop(c)

print(output)
