coffee_counter = 0

while True:
    word = input()
    if word == "END":
        break
    elif word == "cat" or word == "dog" or word == "coding" or word == "movie":
        coffee_counter += 1
    elif word == "CAT" or word == "DOG" or word == "CODING" or word == "MOVIE":
        coffee_counter += 2
    else:
        continue

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)
