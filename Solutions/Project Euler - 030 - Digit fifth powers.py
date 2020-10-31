# ------------------------------------------------------------------------------
# Project Euler - Problem 030 - Digit fifth powers
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=030
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
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

def isfifthSum(n):
    num = n
    fifthsum = 0
    while num > 0:
        fifthsum += (num % 10)**5
        num = int (num/10)
    return fifthsum == n


fifth = []
for i in range(2, 300000):
    if isfifthSum(i):
        fifth += [i]

print (fifth, sum(fifth))
