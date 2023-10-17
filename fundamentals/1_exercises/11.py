budget = float(input())
price_flour_1_kg = float(input())
price_of_1_pack_of_eggs = 0.75 * price_flour_1_kg
price_of_1_l_milk = 1.25 * price_flour_1_kg
counter_bread = 0
counter_colored_eggs = 0

price_for_1st_making = price_flour_1_kg + price_of_1_pack_of_eggs + (0.25 * price_of_1_l_milk)
while budget > price_for_1st_making:
    budget -= price_for_1st_making
    counter_bread += 1
    counter_colored_eggs += 3
    if counter_bread % 3 == 0:
        counter_colored_eggs -= (counter_bread - 2)

print(f"You made {counter_bread} loaves of Easter bread! Now you have {counter_colored_eggs} eggs and {budget:.2f}"
      f"BGN left.")
