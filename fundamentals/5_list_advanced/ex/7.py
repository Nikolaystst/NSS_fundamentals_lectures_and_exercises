seq_of_nums = [int(x) for x in input().split(", ")]
group = 0

while seq_of_nums:
    group += 10
    nums_to_print = [x for x in seq_of_nums if x <= group]
    seq_of_nums = [x for x in seq_of_nums if x > group]
    print(f"Group of {group}'s: {nums_to_print}")
