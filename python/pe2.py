def fibonacciSum(limit, divisor=1):
    fib1 = 1
    fib2 = 2
    total = 0
    while fib2 < limit:
        if fib1%divisor == 0:
            total += fib1
        if fib2%divisor == 0:
            total += fib2
        fib1 += fib2
        fib2 += fib1
    if fib1 < limit:
        total += fib1
    return total

print fibonacciSum(4000000, divisor=2)

print fibonacciSum(1000)
