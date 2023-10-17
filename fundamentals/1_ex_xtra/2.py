word = input()

my_list = []

for i, y in enumerate(word):
    if y.isupper():
        my_list.append(i)

print(my_list)
