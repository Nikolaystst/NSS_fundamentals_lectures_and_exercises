import math

employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())

students_count = int(input())

employee_efficiency = employee_1 + employee_2 + employee_3

hours_count = math.ceil(students_count / employee_efficiency)

if hours_count % 3 != 0:
    employee_breaks = math.floor(hours_count / 3)
else:
    employee_breaks = math.floor(hours_count / 3) - 1

hours_count += employee_breaks

if hours_count < 0:
    hours_count = 0

print(f"Time needed: {hours_count}h.")
