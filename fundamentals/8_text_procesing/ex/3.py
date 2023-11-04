text = input().split("\\")
one, two = text[len(text) - 1].split(".")
print(f'File name: {one}')
print(f'File extension: {two}')
