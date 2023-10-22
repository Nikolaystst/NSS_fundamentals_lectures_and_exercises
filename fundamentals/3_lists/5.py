num = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []

for i in range(num):
    number = int(input())

    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

filter_1 = input()

if filter_1 == "even":
    print(even_list)
elif filter_1 == "odd":
    print(odd_list)
elif filter_1 == "positive":
    print(positive_list)
else:
    print(negative_list)
