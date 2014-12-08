def digit_sum(n):
    sum = 0
    for x in str(n):
        sum += int(x)
    return sum

def factorial(x):
    x * (x - 1)
    x -= 1