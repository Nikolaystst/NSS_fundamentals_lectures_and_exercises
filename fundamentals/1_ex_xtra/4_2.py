my_list = ["ferrari", "merc", "bmw", "lambo"]
word = input()
word = word.lower()

for i in my_list:
    print(f"The manufacturers in this years 24h of le man are: {word.count(i)}")
