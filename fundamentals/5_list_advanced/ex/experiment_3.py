# word_to_merge = input().split()
# index = int(input())
# partition = int(input())
# the_word_in_list = list(word_to_merge[index])
# letters_in_partition = len(word_to_merge[index]) // partition
# word_to_merge.pop(index)
#
# for i in range(partition):
#     the_letters_to_append = the_word_in_list[0:letters_in_partition]
#     the_word_in_list = the_word_in_list[letters_in_partition:]
lst = ["aust", "maust", "baust"]
title = "kore4i"
lst = lst + [title] + [f"{title}-Exercise"]
print(lst)