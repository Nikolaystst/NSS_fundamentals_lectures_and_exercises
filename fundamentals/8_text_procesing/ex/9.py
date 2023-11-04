def word_to_capitalize(word):
    word_to_print = ""
    final_word = ""
    letter = 0
    while word:
        if not word[letter].isdigit():
            word_to_print += word[letter]
        elif letter < len(word) - 1 and word[letter].isdigit() and word[letter + 1].isdigit():
            final_word += word_to_print.upper() * int(f"{word[letter]}{word[letter + 1]}")
            word_to_print = ""
        else:
            final_word += word_to_print.upper() * int(word[letter])
            word_to_print = ""
        word = word[1:]
    return final_word


word = input()
nss = set(word_to_capitalize(word))
print(f"Unique symbols used: {len(nss)}")
print(word_to_capitalize(word))
