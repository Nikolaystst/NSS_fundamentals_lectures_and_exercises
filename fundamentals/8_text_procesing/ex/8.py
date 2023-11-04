def sum_alpha(word):
    sum_1 = 0
    first_letter = word[0]
    last_letter = word[len(word) - 1]
    number = int(word[1:len(word) - 1])

    if first_letter.isupper():
        sum_1 += number / (ord(first_letter) - 64)
    elif first_letter.islower():
        sum_1 += number * (ord(first_letter) - 96)

    if last_letter.isupper():
        sum_1 -= ord(last_letter) - 64
    elif last_letter.islower():
        sum_1 += ord(last_letter) - 96

    return sum_1


total_sum = 0
string = input().split()

for word in string:
    total_sum += sum_alpha(word)

print(f'{total_sum:.2f}')
