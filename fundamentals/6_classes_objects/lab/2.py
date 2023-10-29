class Party:

    def __init__(self):
        self.people = []

    def lst_append(self, name):
        self.people.append(name)

    def names(self):
        return f"Going: {', '.join(self.people)}"

    def lenght(self):
        return f"Total: {len(self.people)}"


party = Party()
while True:
    command = input()
    if command == "End":
        break
    Party.lst_append(party, command)

print(party.names())
print(party.lenght())
