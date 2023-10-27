nss_lst = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "End":
        break
    else:
        command = command.split()
        command_to_use = command[0]
        index = int(command[1])
        v_p_r = int(command[2])

    if command_to_use == "Shoot":
        if index < 0 or index >= len(nss_lst):
            continue
        else:
            nss_lst[index] = nss_lst[index] - v_p_r
            if nss_lst[index] <= 0:
                nss_lst.pop(index)

    elif command_to_use == "Add":
        if index < 0 or index >= len(nss_lst):
            print("Invalid placement!")
        else:
            nss_lst.insert(index, v_p_r)

    elif command_to_use == "Strike":
        if (index - v_p_r) < 0 or (index + v_p_r) >= len(nss_lst):
            print("Strike missed!")
        else:
            nss_lst = nss_lst[:(index - v_p_r)] + nss_lst[(index + v_p_r + 1):]

nss_lst = [str(x) for x in nss_lst]
print("|".join(nss_lst))
