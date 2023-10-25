def letter_to_letter(letter_one, letter_two):
    num_one = ord(letter_one)
    num_two = ord(letter_two)
    result = ""
    for i in range(num_one + 1, num_two):
        result += f"{chr(i)} "
    return result


first_letter = input()
second_letter = input()
print(letter_to_letter(first_letter, second_letter))
