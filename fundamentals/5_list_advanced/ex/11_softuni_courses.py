def add_lesson(lst, title):
    if title not in lst:
        lst = lst + [title]
    return lst


def insert_lesson_at_index(lst, title, index):
    if title not in lst:
        lst.insert(int(index), title)
    return lst


def remove_lesson(lst, title):
    if title in lst:
        lst.remove(title)
        if f"{title}-Exercise" in lst:
            lst.remove(f"{title}-Exercise")
    return lst


def swap_lessons(lst, title_1, title_2):
    if title_1 in lst and title_2 in lst:
        index_1 = lst.index(title_1)
        index_2 = lst.index(title_2)
        lst[index_1], lst[index_2] = lst[index_2], lst[index_1]
        if f"{title_1}-Exercise" in lst and f"{title_2}-Exercise" not in lst:
            index_1 = lst.index(title_1)
            index_2 = lst.index(f"{title_1}-Exercise")
            lst.insert(index_1 + 1, f"{title_1}-Exercise")
            lst.pop(index_2)
        elif f"{title_2}-Exercise" in lst and f"{title_1}-Exercise" not in lst:
            index_1 = lst.index(title_2)
            index_2 = lst.index(f"{title_2}-Exercise")
            lst.insert(index_1 + 1, f"{title_2}-Exercise")
            lst.pop(index_2 + 1)
        elif f"{title_1}-Exercise" in lst and f"{title_2}-Exercise" in lst:
            index_1 = lst.index(f"{title_1}-Exercise")
            index_2 = lst.index(f"{title_2}-Exercise")
            lst[index_1], lst[index_2] = lst[index_2], lst[index_1]
    return lst


def add_leson_exercise(lst, title):
    if title in lst and f"{title}-Exercise" not in lst:
        index_1 = lst.index(title)
        lst.insert(index_1 + 1, f"{title}-Exercise")
    elif title not in lst:
        lst = lst + [title] + [f"{title}-Exercise"]
    return lst


def print_idx(lst):
    for i, c in enumerate(lst):
        print(f"{i + 1}.{c}")


softuni_courses = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    command = command.split(":")
    if command[0] == "Add":
        softuni_courses = add_lesson(softuni_courses, command[1])
    elif command[0] == "Insert":
        softuni_courses = insert_lesson_at_index(softuni_courses, command[1], command[2])
    elif command[0] == "Remove":
        softuni_courses = remove_lesson(softuni_courses, command[1])
    elif command[0] == "Swap":
        softuni_courses = swap_lessons(softuni_courses, command[1], command[2])
    else:
        softuni_courses = add_leson_exercise(softuni_courses, command[1])

print_idx(softuni_courses)
