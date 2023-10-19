num = int(input())

for i in range(num):
    for y in range(num):
        for u in range(num):
            print(f"{chr(97 + i)}{chr(97 + y)}{chr(97 + u)}")
