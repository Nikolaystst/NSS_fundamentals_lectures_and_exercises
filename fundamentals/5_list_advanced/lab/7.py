def happy_func(lst, fact):
    full_happines = 0
    for i in lst:
        full_happines += int(i)
    full_happines *= fact
    full_happines /= len(lst)
    lst = [int(x) * fact for x in lst]
    employ_happy = [x for x in lst if x > full_happines]
    if len(employ_happy) >= len(lst) / 2:
        return f"Score: {len(employ_happy)}/{len(lst)}. Employees are happy!"
    else:
        return f"Score: {len(employ_happy)}/{len(lst)}. Employees are not happy!"


employ_happ = input().split()
factor = int(input())
print(happy_func(employ_happ, factor))
