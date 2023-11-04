def final_msg(lst, word):
    final_word = ""
    index = 0

    for letter in word:
        new_letter = chr(ord(letter) - lst[index])
        final_word += new_letter
        index = (index + 1) % len(lst)

    precious_start = final_word.find("&") + 1
    precious_end = final_word.find("&", precious_start)
    coord_start = final_word.find("<") + 1
    coord_end = final_word.find(">")

    return f"Found {final_word[precious_start:precious_end]} at {final_word[coord_start:coord_end]}"


nss_lst = [int(x) for x in input().split()]
while True:
    message = input()
    if message == "find":
        break
    print(final_msg(nss_lst, message))
