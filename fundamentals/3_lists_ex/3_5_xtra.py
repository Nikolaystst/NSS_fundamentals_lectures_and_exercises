row_1 = input().split()
row_2 = input().split()
row_3 = input().split()

flag_1 = False
flag_2 = False

if row_1[1] == row_1[0] and row_1[0] == row_1[2]:
    if row_1[0] == "2":
        flag_2 = True
    elif row_1[0] == "1":
        flag_1 = True
elif row_2[1] == row_2[0] and row_2[0] == row_2[2]:
    if row_2[0] == "2":
        flag_2 = True
    elif row_2[0] == "1":
        flag_1 = True
elif row_3[1] == row_3[0] and row_3[0] == row_3[2]:
    if row_3[0] == "2":
        flag_2 = True
    elif row_3[0] == "1":
        flag_1 = True
elif row_1[0] == row_2[0] and row_1[0] == row_3[0]:
    if row_1[0] == "1":
        flag_1 = True
    elif row_1[0] == "2":
        flag_2 = True
elif row_1[1] == row_2[1] and row_1[1] == row_3[1]:
    if row_1[1] == "1":
        flag_1 = True
    elif row_1[1] == "2":
        flag_2 = True
elif row_1[2] == row_2[2] and row_1[2] == row_3[2]:
    if row_1[2] == "1":
        flag_1 = True
    elif row_1[2] == "2":
        flag_2 = True
elif row_1[0] == row_2[1] and row_1[0] == row_3[2]:
    if row_1[0] == "1":
        flag_1 = True
    elif row_1[0] == "2":
        flag_2 = True
elif row_1[2] == row_2[1] and row_1[2] == row_3[0]:
    if row_1[2] == "1":
        flag_1 = True
    elif row_1[2] == "2":
        flag_2 = True

if flag_1:
    print("First player won")
elif flag_2:
    print("Second player won")
else:
    print("Draw!")
