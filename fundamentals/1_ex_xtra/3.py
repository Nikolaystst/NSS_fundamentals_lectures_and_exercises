my_list = input().split(", ")
my_list.reverse()

if my_list[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for e, c in enumerate(my_list):
        if c == "wolf":
            print(f"Oi! Sheep number {e}! You are about to be eaten by a wolf!")
