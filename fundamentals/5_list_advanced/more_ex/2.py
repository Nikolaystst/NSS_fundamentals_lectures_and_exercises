full_list = list(input())
list_of_nums = [int(x) for x in full_list if x.isdigit()]
list_of_taken = []
for c, i in enumerate(list_of_nums):
    if c % 2 == 0:
        list_of_taken.append(i)
list_of_skipped = []
for c, i in enumerate(list_of_nums):
    if c % 2 != 0:
        list_of_skipped.append(i)
list_of_letters = [x for x in full_list if not x.isdigit()]

list_of_taken_to_append = []
list_of_taken_to_skip = []
flag = False

for b in range(len(list_of_taken)):
    taken_in_loop = list_of_taken[b]
    if flag:
        break
    for y in range(taken_in_loop):
        list_of_taken_to_append.append(list_of_letters[0])
        list_of_letters.pop(0)
        if not list_of_letters:
            flag = True
            break
    if flag:
        break
    skipped_in_loop = list_of_skipped[b]
    for y in range(skipped_in_loop):
        list_of_taken_to_skip.append(list_of_letters[0])
        list_of_letters.pop(0)
        if not list_of_letters:
            break


print("".join(list_of_taken_to_append))
