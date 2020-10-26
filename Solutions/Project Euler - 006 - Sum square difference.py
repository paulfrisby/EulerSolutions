# ------------------------------------------------------------------------------
# Project Euler - Problem 006 - Sum square difference
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=006
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2+...+10^2 = 385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# when power = n, returns sum of nth powers up to limit
def sumOfPowers(power, limit):
    runningSum = 0
    for i in range(1, limit + 1):
        runningSum += i**power
    return runningSum


# when power = n, returns nth power of sum of n up to limit
def powerOfSums(power, limit):
    runningSum = 0
    for i in range(1, limit + 1):
        runningSum += i
    return runningSum**power

def diffOfPowers(power, limit):
    return powerOfSums(power, limit) - sumOfPowers(power, limit)

print (diffOfPowers(2, 100))
