# word = input()
# b = ""
# for i in word:
#     if i.isdigit():
#         b += i
#
# print(b)
# command_given = input().split()
#
# command, start_index_or_index, end_index_or_partition = command_given[0], command_given[1], command_given[2]
#
# print(command, start_index_or_index, end_index_or_partition)
# word_to_merge = input().split()
# start_index = int(input())
# end_index = int(input())
# if end_index > len(word_to_merge) - 1:
#     end_index = len(word_to_merge) - 1
#
# if start_index == 0:
#     word_to_merge = ["".join(word_to_merge[start_index:end_index + 1])] + word_to_merge[end_index + 1:]
#     print(word_to_merge)
# else:
#     word_to_merge = word_to_merge[:start_index] + ["".join(word_to_merge[start_index:end_index + 1])]
#     + word_to_merge[end_index + 1:]
#     print(word_to_merge)

word_to_merge = input().split()
index = int(input())
partition = int(input())
the_word_in_list = list(word_to_merge[index])
letters_in_partition = len(word_to_merge[index]) // partition
word_to_merge.pop(index)

for i in range(partition):
    if i == partition - 1:
        the_letters_to_append = "".join(the_word_in_list)
        word_to_merge.insert(index + i, the_letters_to_append)
    else:
        the_letters_to_append = "".join(the_word_in_list[0:letters_in_partition])
        the_word_in_list = the_word_in_list[letters_in_partition:]
        word_to_merge.insert(index + i, the_letters_to_append)



print(word_to_merge)