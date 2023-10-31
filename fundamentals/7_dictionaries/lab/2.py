# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes

word = input().split()
nss_dict = {}

for idx in range(0, len(word), 2):
    key = word[idx]
    value = int(word[idx + 1])
    nss_dict[key] = value

nss_lst = input().split()

for i in nss_lst:
    if i in nss_dict.keys():
        print(f'We have {nss_dict[i]} of {i} left')
    else:
        print(f"Sorry, we don't have {i}")
