word = input()
word_to_print = ""
nums_to_print = ""

for letter in word:

    if not letter.isdigit():
        word_to_print += letter.upper()
        nums_to_print += " "
    else:
        nums_to_print += letter
        word_to_print += " "

word_to_print = word_to_print.split()
nums_to_print = nums_to_print.split()
nss = set("".join(word_to_print))
print(f"Unique symbols used: {len(nss)}")
for i in range(len(word_to_print)):
    print(f"{word_to_print[i] * int(nums_to_print[i])}", end="")
