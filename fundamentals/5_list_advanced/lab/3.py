my_list = []
def list_appending():
    while True:
        command = input()
        if command == "End":
            return my_list
        command = command.split("-")
        my_list.append([command[0], command[1]])


def sorted_list_appending(lst):
    lst = sorted(lst)
    sorted_list = [x[1] for x in lst]
    return sorted_list


print(sorted_list_appending(list_appending()))
