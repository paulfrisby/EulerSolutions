# ------------------------------------------------------------------------------
# Project Euler - Problem 021 - Amicable numbers
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=021
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
general outline / plan of approach to problem
explanation of insights in to problem may also be included here as necessary
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Extra Information
# ------------------------------------------------------------------------------
"""
optional section depending on problem
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

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

print (sumAmicable(10000))
