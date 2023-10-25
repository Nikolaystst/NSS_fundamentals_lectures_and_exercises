def nic_func(lst):
    result = True
    counter = 0
    if 6 > len(lst) or len(lst) > 10:
        result = False
        print("Password must be between 6 and 10 characters")

    for i in lst:
        if 48 <= ord(i) <= 57 or 97 <= ord(i) <= 122:
            continue
        else:
            result = False
            print("Password must consist only of letters and digits")
            break

    for i in lst:
        if 48 <= ord(i) <= 57:
            counter += 1
    if counter < 2:
        result = False
        print("Password must have at least 2 digits")

    if result:
        print("Password is valid")


pass_word = input().lower()
my_list = []
for i in pass_word:
    my_list.append(i)

nic_func(my_list)
