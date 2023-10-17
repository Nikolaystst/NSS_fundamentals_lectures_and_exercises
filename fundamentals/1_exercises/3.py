num_zero = int(input())

for i in range(num_zero):
    num = input()
    if num == "88":
        print("Hello")
    elif num == "86":
        print("How are you?")
    elif int(num) < 88:
        print("GREAT!")
    else:
        print("Bye.")