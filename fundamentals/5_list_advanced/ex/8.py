def num_to_letter(word_to_transform):
    digit_to_char = ""
    for c, i in enumerate(word_to_transform):
        if i.isdigit():
            digit_to_char += i
            word_to_transform = word_to_transform[1:]
    digit_to_char = chr(int(digit_to_char))
    word_to_transform = digit_to_char + word_to_transform
    return word_to_transform


def second_to_last(word):
    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    word = "".join(word)
    return word


word_to_split = input().split()
final_words = []
true_final_words = []
word_to_transform = ""
for i in range(0, len(word_to_split)):
    word_to_transform = word_to_split[i]
    final_words.append(num_to_letter(word_to_transform))
    true_final_words.append(second_to_last(final_words[i]))

print(" ".join(true_final_words))
