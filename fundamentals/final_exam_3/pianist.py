nss_dict = {}
n = int(input())

for _ in range(n):
    lst = input().split("|")
    nss_dict[lst[0]] = {"composer": lst[1], "key": lst[2]}

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("|")

    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in nss_dict.keys():
            print(f"{piece} is already in the collection!")
        elif piece not in nss_dict.keys():
            nss_dict[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece not in nss_dict.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        elif piece in nss_dict.keys():
            del nss_dict[piece]
            print(f"Successfully removed {piece}!")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece not in nss_dict.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        elif piece in nss_dict.keys():
            nss_dict[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

for piece, val in nss_dict.items():
    print(f"{piece} -> Composer: {val['composer']}, Key: {val['key']}")
