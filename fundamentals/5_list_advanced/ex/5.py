rows = int(input())
all_ppl = 0
all_chairs = 0
flag = False
for i in range(1, rows + 1):
    set_1 = input().split()
    chairs = set_1[0]
    all_chairs += len(chairs)
    ppl = int(set_1[1])
    all_ppl += ppl
    if ppl > len(chairs):
        print(f"{ppl - len(chairs)} more chairs needed in room {i}")
        flag = True
if not flag:
    print(f"Game On, {all_chairs - all_ppl} free chairs left")
