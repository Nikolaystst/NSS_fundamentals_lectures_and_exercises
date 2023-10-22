num = int(input())
list_positives= []
list_negatives= []

for i in range(num):
    number_2 = int(input())
    if number_2 >= 0:
        list_positives.append(number_2)
    else:
        list_negatives.append(number_2)

print(list_positives)
print(list_negatives)
print(f"Count of positives: {len(list_positives)}")
print(f"Sum of negatives: {sum(list_negatives)}")