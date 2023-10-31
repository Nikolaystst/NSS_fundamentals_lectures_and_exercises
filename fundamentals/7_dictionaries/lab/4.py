# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals

# Alex:6:programming basics
# Maria:7:programming basics
# Kaloyan:9:advanced
# Todor:10:fundamentals
# programming_basics


nss_dict = {}
command = input().split(":")
while len(command) > 1:
    key, value, course = command[0], command[1], command[2]
    if course not in nss_dict.keys():
        nss_dict[course] = []
    nss_dict[course].append(f"{key} - {value}")
    command = input().split(":")

command = command[0].replace("_", " ")
# print(nss_dict) ako iska6 da go razbere6 mahni hashtaga
for student in nss_dict[command]:
    print(student)
