key = int(input())
num_letters = int(input())

for i in range(num_letters):
    letter = input()
    letter = ord(letter) + key
    letter = chr(letter)
    print(letter, end="")
