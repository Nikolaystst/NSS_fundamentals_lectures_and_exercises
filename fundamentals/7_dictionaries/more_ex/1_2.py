contests = {}  # dictionary to store contests and passwords
submissions = {}  # dictionary to store user points for each contest

# read input until "end of contests"
while True:
    line = input().strip()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contests[contest] = password

# read input until "end of submissions"
while True:
    line = input().strip()
    if line == "end of submissions":
        break
    contest, password, user, points = line.split("=>")
    if contest in contests and contests[contest] == password:
        points = int(points)
        if user not in submissions:
            submissions[user] = {}
        if contest not in submissions[user] or points > submissions[user][contest]:
            submissions[user][contest] = points

# calculate total points for each user
total_points = {}
for user, contests in submissions.items():
    total_points[user] = sum(contests.values())

# print best candidate
best_user, best_points = max(total_points.items(), key=lambda x: x[1])
print(f"Best candidate is {best_user} with total {best_points} points.")

# print all users ordered by name
for user in sorted(submissions.keys()):
    print(user)
    for contest, points in sorted(submissions[user].items(), key=lambda x: (-x[1], x[0])):
        print(f"#  {contest} -> {points}")
