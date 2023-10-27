def nic_func(lst):
    lst = [int(x) for x in lst]
    positive_list = [str(x) for x in lst if x >= 0]
    negative_list = [str(x) for x in lst if x < 0]
    even_list = [str(x) for x in lst if x % 2 == 0]
    odd_list = [str(x) for x in lst if x % 2 != 0]
    print(f"Positive: {', '.join(positive_list)}")
    print(f"Negative: {', '.join(negative_list)}")
    print(f"Even: {', '.join(even_list)}")
    print(f"Odd: {', '.join(odd_list)}")


number = input().split(", ")
nic_func(number)
