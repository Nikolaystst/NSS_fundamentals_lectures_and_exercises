def nic_func(w_1, w_n_2):
    if w_1 == "int":
        return int(float(w_n_2) * 2)
    elif w_1 == "real":
        return f"{(float(w_n_2) * 1.5):.2f}"
    else:
        return f"${w_n_2}$"


word = input()
num_letter = input()
print(nic_func(word, num_letter))
