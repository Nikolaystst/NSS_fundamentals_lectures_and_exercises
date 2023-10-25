def nikey_func(lst):
    for i in lst:
        if i[:] == i[::-1]:
            print(True)
        else:
            print(False)


word = input().split(", ")
nikey_func(word)
