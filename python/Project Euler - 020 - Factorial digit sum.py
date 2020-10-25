def sumOfDigits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n / 10
    return total

def factorial(n):
    total = 1
    while n > 0:
        total = total * n
        n -= 1
    return total

print sumOfDigits( factorial(100) )
