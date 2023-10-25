def output(grade):
    if 2 <= grade <= 2.99:
        result = "Fail"
    elif 3 <= grade <= 3.49:
        result = "Poor"
    elif 3.50 <= grade <= 4.49:
        result = "Good"
    elif 4.5 <= grade <= 5.49:
        result = "Very Good"
    else:
        result = "Excellent"
    return result


mark = float(input())
print(output(mark))
