char_1 = input()
char_2 = input()
word = input()
range_1 = ord(char_1)
range_2 = ord(char_2)
sum_1 = 0
for i in word:
    if range_1 < ord(i) < range_2:
        sum_1 += ord(i)
print(sum_1)
