nss_lst = [int(x) for x in input().split()]
nss_lst_2 = []
average = sum(nss_lst) / len(nss_lst)
for i in range(len(nss_lst)):
    if nss_lst[i] >= average:
        nss_lst_2.append(nss_lst[i])

nss_lst_2.sort()

print(average)
print(nss_lst_2)
print(nss_lst_2[-1:-6:-1])
