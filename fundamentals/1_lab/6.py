budget = int(input())
all_bought = 0

while True:
    bought = input()
    if bought == "End" and all_bought <= budget:
        print("You bought everything needed.")
        break

    all_bought += int(bought)

    if all_bought > budget:
        print("You went in overdraft!")
        break