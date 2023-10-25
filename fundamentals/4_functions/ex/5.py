def output_func(integer_1):
    if integer_1 % 2 != 0:
        return False
    else:
        return True


nums = input().split()
nums = [int(x) for x in nums]
nums_2 = []
even = filter(output_func, nums)

for i in even:
    nums_2.append(i)

print(nums_2)
