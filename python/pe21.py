def sumOfDivisors(n):
    if n < 2:
        return 0
    total = 1
    divisor = 2
    while divisor**2 - 1 < n:
        if n % divisor == 0:
            total += divisor
            if n / divisor != divisor:
                total += n / divisor
        divisor += 1
    return total

def sumAmicable(lim):
    total = 0
    for i in range(lim):
        if sumOfDivisors(sumOfDivisors(i)) == i and i != sumOfDivisors(i):
            total += i
    return total

print sumAmicable(10000)
    
