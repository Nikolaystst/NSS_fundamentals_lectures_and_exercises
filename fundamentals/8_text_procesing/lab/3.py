word_to_filter = input()
word_in_which_filter = input()

while word_to_filter in word_in_which_filter:
    word_in_which_filter = word_in_which_filter.replace(word_to_filter, "")

print(word_in_which_filter)
