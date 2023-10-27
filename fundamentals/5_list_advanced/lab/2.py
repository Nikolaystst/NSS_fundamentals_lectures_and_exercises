def nic_func(lst_wagons):
    while True:
        command = input()
        if command == "End":
            return lst_wagons
        command = command.split()
        if command[0] == "add":
            lst_wagons[-1] += int(command[1])
        elif command[0] == "insert":
            lst_wagons[int(command[1])] += int(command[2])
        else:
            lst_wagons[int(command[1])] -= int(command[2])


wagons = int(input())
list_wagons = [0] * wagons
print(nic_func(list_wagons))
