times = int(input())

for i in range(times):
    string = input().split()
    name = ""
    years = ""
    for word in string:
        if "@" in word and "|" in word:
            name = word[word.find("@") + 1:word.find("|")]
        elif "#" in word and "*" in word:
            years = word[word.find("#") + 1:word.find("*")]
    print(f"{name} is {years} years old.")