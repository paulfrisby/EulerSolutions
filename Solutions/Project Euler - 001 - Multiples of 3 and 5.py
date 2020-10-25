def sumOfMultiples(mult1, mult2, limit):
    sum = 0
    for x in range(limit):
        if x%mult1 == 0 or x%mult2 == 0:
            sum += x
    return sum

print sumOfMultiples(3, 5, 1000)
