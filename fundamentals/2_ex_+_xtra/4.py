num_of_rows = int(input())
sum_of_ints = 0

for i in range(num_of_rows):
    char = input()
    char_int = ord(char)
    sum_of_ints += char_int

print(f"The sum equals: {sum_of_ints}")
