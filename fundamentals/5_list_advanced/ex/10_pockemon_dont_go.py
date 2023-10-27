seq_input = [int(x) for x in input().split()]
seq_to_sum = []
inx_value = 0

while seq_input:
    index_manipulation = int(input())
    if index_manipulation < 0:
        inx_value = seq_input[0]
        seq_input.pop(0)
        seq_input.insert(0, seq_input[len(seq_input) - 1])
        seq_to_sum.append(inx_value)
        for i, c in enumerate(seq_input):
            if c <= inx_value:
                c += inx_value
                seq_input.pop(i)
                seq_input.insert(i, c)
            else:
                c -= inx_value
                seq_input.pop(i)
                seq_input.insert(i, c)
    elif index_manipulation >= len(seq_input):
        inx_value = seq_input[-1]
        seq_input.insert(-1, seq_input[0])
        seq_input.pop(-1)
        seq_to_sum.append(inx_value)
        for i, c in enumerate(seq_input):
            if c <= inx_value:
                c += inx_value
                seq_input.pop(i)
                seq_input.insert(i, c)
            else:
                c -= inx_value
                seq_input.pop(i)
                seq_input.insert(i, c)
    else:
        inx_value = seq_input[index_manipulation]
        seq_input.pop(index_manipulation)
        seq_to_sum.append(inx_value)
        for i, c in enumerate(seq_input):
            if c <= inx_value:
                c += inx_value
                seq_input.pop(i)
                seq_input.insert(i, c)
            else:
                c -= inx_value
                seq_input.pop(i)
                seq_input.insert(i, c)

print(sum(seq_to_sum))
