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
# Optimisation
# ------------------------------------------------------------------------------
"""
Originally this was taking quite a while to compute. This was because
sumOfDivisors() was iterating through every possible divisor up to half of n.

Only checking divisors up to square root of n, and adding the divisor and its
inverse in 1 step, is considerably faster. We need to be careful to not double
count a divisor which is the exact square root of n, however.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns sum of all proper divisors of n
def sumOfDivisors(n):

    # 1 is not a proper divisor of 1
    if n < 2:
        return 0
    
    # 1 is a proper divisor of every other natural number
    total = 1
    
    divisor = 2

    # find each divisor up to square root of n, add it and its inverse to total
    while divisor**2 <= n:
        if n % divisor == 0:
            total += divisor
            total += n / divisor

            # remove duplicate if divisor is square root of n
            if divisor**2 == n:
                total -= n / divisor
                
        divisor += 1
        
    return total


# returns list of amicable numbers up to limit
def amicableNumbers(lim):
    numbers = []
    for i in range(lim):
        if sumOfDivisors(sumOfDivisors(i)) == i and i != sumOfDivisors(i):
            numbers.append(i)
    return numbers


print (f'The sum of all amicable numbers under 10,000 is {sum(amicableNumbers(10000))}')
