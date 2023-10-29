class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammal = []
        self.fish = []
        self.bird = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammal.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.bird.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == "mammal":
            result += f'Mammals in {self.name}: {", ".join(self.mammal)}\n'
        elif species == "fish":
            result += f'Fishes in {self.name}: {", ".join(self.mammal)}\n'
        elif species == "bird":
            result += f'Birds in {self.name}: {", ".join(self.mammal)}\n'
        result += f'Total animals: {Zoo.__animals}'

        return result


zoo = Zoo(input())
rounds_of_cycle = int(input())
for i in range(rounds_of_cycle):
    specie_animal = input().split()
    zoo.add_animal(specie_animal[0], specie_animal[1])

print(zoo.get_info(input()))
