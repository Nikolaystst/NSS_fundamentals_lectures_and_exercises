def my_func(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    print("\n".join(lst))


word = input().split()
my_func(word)
