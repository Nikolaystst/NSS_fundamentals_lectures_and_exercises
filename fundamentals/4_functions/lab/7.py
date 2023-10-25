def output(string):
    string = [float(x) for x in string]
    string = [round(x) for x in string]
    return string


word = input().split()
print(output(word))
