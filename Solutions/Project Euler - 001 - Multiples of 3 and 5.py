# ------------------------------------------------------------------------------
# Project Euler - Problem 001 - Multiples of 3 and 5
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=001
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
runningSum = 0

for each number below 1000:
    if (number is divisible by 3) or (number is divisible by 5)
        runningSum = runningSum + number
        
print runningSum
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# sums the multiples of any 2 numbers up to a given limit
def sumOfMultiples(mult1, mult2, limit):
    runningSum = 0
    for x in range(limit):
        if x%mult1 == 0 or x%mult2 == 0:
            runningSum += x
    return runningSum

print (sumOfMultiples(3, 5, 1000))
