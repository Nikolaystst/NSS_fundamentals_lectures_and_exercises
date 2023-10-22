num = int(input())
filter_word = input()
my_list = []
filtered_list = []

for i in range(num):
    word_appending = input()
    my_list.append(word_appending)
    if filter_word in word_appending:
        filtered_list.append(word_appending)

print(my_list)
print(filtered_list)
