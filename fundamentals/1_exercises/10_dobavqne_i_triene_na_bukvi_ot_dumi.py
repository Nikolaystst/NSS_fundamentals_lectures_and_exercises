word_1 = input()
word_2 = input()
word_2_final = ""
final_word = ""
final_word_2 = ""

for i in word_2:
    word_2_final += i
    # ^ dobavqm po edin simvol ot 2rata duma vsqko izpylnenie na cikyla
    word_1 = word_1[1::]
    # ^ vadq po edin simvol ot 1vata duma vsqko izpylnenie na cikyla
    final_word = word_2_final + word_1
    # ^ krainata duma e ravna na sbora mi ot 2te ostanali za vseki cikyl
    if final_word_2 == final_word:
        continue
    else:
        final_word_2 = final_word
# ^ sravnqvam dali starata i novata duma sa printirani i ako sa po4vam na novo cikyla ina4e printiram unikalen resultat
        print(final_word)
