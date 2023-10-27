def nic_func(string_1, lst_filter):
    list_filtered = [x for x in string_1 if x.lower() not in lst_filter]
    return "".join(list_filtered)


list_vowels = ['a', 'o', 'u', 'e', 'i']
word = list(input())
print(nic_func(word, list_vowels))
