def output(string, repeater_1):
    result = string * repeater_1
    return result


word = input()
repeater = int(input())
print(output(word, repeater))
