nss_lst = [int(x) for x in input().split(", ")]
entry_index = int(input())
command = input()

nss_left = nss_lst[:entry_index]
nss_right = nss_lst[entry_index + 1:]
the_given_price = nss_lst[entry_index]
sum_of_left = 0
sum_of_right = 0

if command == "cheap":
    nss_left = [x for x in nss_left if x < the_given_price]
    nss_right = [x for x in nss_right if x < the_given_price]
    sum_of_left = sum(nss_left)
    sum_of_right = sum(nss_right)

elif command == "expensive":
    nss_left = [x for x in nss_left if x >= the_given_price]
    nss_right = [x for x in nss_right if x >= the_given_price]
    sum_of_left = sum(nss_left)
    sum_of_right = sum(nss_right)

if sum_of_left >= sum_of_right:
    print(f"Left - {sum_of_left}")
else:
    print(f"Right - {sum_of_right}")
