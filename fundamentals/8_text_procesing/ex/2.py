word_1, word_2 = input().split()
sumed_charackter = 0

if len(word_1) > len(word_2):
    for i in range(0, len(word_1)):
        if i <= len(word_2) - 1:
            sumed_charackter += (ord(word_1[i]) * ord(word_2[i]))
        else:
            sumed_charackter += ord(word_1[i])

elif len(word_2) > len(word_1):
    for i in range(0, len(word_2)):
        if i <= len(word_1) - 1:
            sumed_charackter += (ord(word_1[i]) * ord(word_2[i]))
        else:
            sumed_charackter += ord(word_2[i])

else:
    for i in range(0, len(word_1)):
        sumed_charackter += (ord(word_1[i]) * ord(word_2[i]))

print(sumed_charackter)
