# a, b, c, a
word = input().split(", ")
nss_dict = {x: ord(x) for x in word}
print(nss_dict)
