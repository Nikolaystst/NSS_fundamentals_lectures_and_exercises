list_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
list_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
word = input().split()

for i in range(len(word)):
    if len(list_A) < 7 or len(list_B) < 7:
        break
    if word[i] in list_A:
        list_A.remove(word[i])
    elif word[i] in list_B:
        list_B.remove(word[i])
    else:
        continue

print(f"Team A - {len(list_A)}; Team B - {len(list_B)}")
if len(list_A) < 7 or len(list_B) < 7:
    print("Game was terminated")
