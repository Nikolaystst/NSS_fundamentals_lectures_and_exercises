divisor = int(input())
boundary = int(input())
result = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        result = i

print(result)