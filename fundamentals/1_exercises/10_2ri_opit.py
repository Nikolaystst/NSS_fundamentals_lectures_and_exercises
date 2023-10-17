word_1 = input()
word_2 = input()
final_word = word_1

for i in range(len(word_1)):
    final_word = word_2[:i + 1] + word_1[i + 1:]
    if word_2[i] == word_1[i]:
        continue
    print(final_word)