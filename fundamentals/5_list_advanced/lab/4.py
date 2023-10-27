def polidrome_func(lst):
    poly_list = [x for x in lst if x[::] == x[::-1]]
    return poly_list


def counter_poly_func(lst, filter_word):
    x = lst.count(filter_word)
    return f"Found palindrome {x} times"


word = input().split()
filter_word = input()
print(polidrome_func(word))
print(counter_poly_func(polidrome_func(word), filter_word))
