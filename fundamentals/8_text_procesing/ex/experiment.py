# word = "aSd2&5s@1"
# final_word = ""
# word_to_print = ""
# for num_1 in range(len(word)):
#
#     if not word[num_1].isdigit():
#         word_to_print += word[num_1]
#     elif word[num_1].isdigit():
#         final_word += word_to_print.upper() * int(word[num_1])
#         word_to_print = ""
# print(final_word)
ticket = "asdfgh"
print(ticket[:int(len(ticket) / 2)])
