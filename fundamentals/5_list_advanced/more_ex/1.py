welth_of_ppl = [int(x) for x in input().split(", ")]
welth_of_ppl_2 = []
min_welth = int(input())
chico_skruch = max(welth_of_ppl)
index_1 = welth_of_ppl.index(max(welth_of_ppl))
welth_of_ppl.pop(index_1)
flag = False

for i in welth_of_ppl:
    if i < min_welth:
        chico_skruch = chico_skruch - (min_welth - i)
        if chico_skruch < min_welth:
            flag = True
            break
        i = min_welth
        welth_of_ppl_2.append(i)
    else:
        welth_of_ppl_2.append(i)

welth_of_ppl_2.insert(index_1, chico_skruch)

if flag:
    print("No equal distribution possible")
else:
    print(welth_of_ppl_2)
