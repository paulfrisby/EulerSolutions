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
9^5 - 59,049 is the highest 5th power that can contribute to our sum

6 digit numbers have max sum of 5th powers of digits of 6 * 59,043 = 354,294
7 digit numbers have max sum of 5th powers of digits of 7 * 59,043 = 413,343

All 7 digit numbers are large than this, and the situation will only get worse
as we add more digits. Therefore, we only need to check up to 6 digit numbners.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns sum of 5th powers of digits of n
def fifthSum(n):
    fifthSum = 0
    while n > 0:

        # add last digit ^ 5 to sum
        fifthSum += (n%10)**5

        # truncate last digit
        n = int(n/10)
        
    return fifthSum


answers = []
for i in range(10, 300000):
    if fifthSum(i) == i:
        answers += [i]

print (f'The numbers that can be written as the sum of fifth powers of their digits are: {answers}')
print (f'The sum of these is {sum(answers)}')
