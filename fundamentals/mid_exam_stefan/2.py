targets = [int(x) for x in input().split()]
shot_targets = 0

while True:
    current = input()

    if current == "End":
        break

    current = int(current)

    if current < 0 or current >= len(targets):
        continue

    the_target = targets[current]
    shot_targets += 1

    for i in range(len(targets)):
        if targets[i] == -1:
            continue
        elif targets[i] <= the_target:
            targets[i] += the_target
        elif targets[i] > the_target:
            targets[i] -= the_target

    targets[current] = -1

print(f'Shot targets: {shot_targets} -> {" ".join(str(x) for x in targets)}')
