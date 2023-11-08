nss_set = {}

while True:
    towns_ppl_gold = input()
    if towns_ppl_gold == "Sail":
        break
    towns_ppl_gold = towns_ppl_gold.split("||")
    city = towns_ppl_gold[0]
    population = int(towns_ppl_gold[1])
    gold = int(towns_ppl_gold[2])
    if city not in nss_set.keys():
        nss_set[city] = {"Population": population, "Gold": gold}
    elif city in nss_set.keys():
        nss_set[city]["Population"] += population
        nss_set[city]["Gold"] += gold

while True:
    command = input()
    if command == "End":
        break
    command = command.split("=>")
    to_do = command[0]
    if to_do == "Plunder":
        city = command[1]
        population = int(command[2])
        gold = int(command[3])
        nss_set[city]["Population"] -= population
        nss_set[city]["Gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
        if nss_set[city]["Population"] <= 0 or nss_set[city]["Gold"] <= 0:
            print(f"{city} has been wiped off the map!")
            del nss_set[city]

    elif to_do == "Prosper":
        city = command[1]
        gold = int(command[2])
        if gold <= 0:
            print("Gold added cannot be a negative number!")
        elif gold > 0:
            nss_set[city]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {nss_set[city]['Gold']} gold.")

if not nss_set:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(nss_set.keys())} wealthy settlements to go to:")
    for cities, vals in nss_set.items():
        print(f"{cities} -> Population: {vals['Population']} citizens, Gold: {vals['Gold']} kg")
