my_list = ["sun", "water", "fish", "sand"]
word = input()
word = word.lower()
count = 0

for i in my_list:
    count += word.count(i)

print(count)