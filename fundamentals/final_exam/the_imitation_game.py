message = input()

while True:
    code_1 = input()
    if code_1 == "Decode":
        break

    code_1 = code_1.split("|")
    command = code_1[0]
    if command == "Move":
        num_of_let = int(code_1[1])
        message = message[num_of_let:] + message[:num_of_let]
    elif command == "Insert":
        indexing = int(code_1[1])
        letter = code_1[2]
        message = message[:indexing] + letter + message[indexing:]
    elif command == "ChangeAll":
        substr = code_1[1]
        replacement = code_1[2]
        message = message.replace(substr, replacement)

print(f"The decrypted message is: {message}")
