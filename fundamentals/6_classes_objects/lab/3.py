class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


nss_lst = []
while True:
    command = input()
    if command == "Stop":
        break
    command = command.split()
    email = Email(command[0], command[1], command[2])
    nss_lst.append(email)

indexes = [int(x) for x in input().split(", ")]
for x in indexes:
    nss_lst[x].send()

for x in nss_lst:
    print(x.get_info())
