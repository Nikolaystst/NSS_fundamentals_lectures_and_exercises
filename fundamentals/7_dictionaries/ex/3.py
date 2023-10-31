c_list = input().split(", ")
cap_list = input().split(", ")
nss_dict = dict(zip(c_list, cap_list))
for key, val in nss_dict.items():
    print(f"{key} -> {val}")
