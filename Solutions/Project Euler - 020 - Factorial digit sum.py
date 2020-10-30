# ------------------------------------------------------------------------------
# Project Euler - Problem 020 - Factorial digit sum
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=020
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Plan
# ------------------------------------------------------------------------------
"""
Similarly to Problem 16, a naive approach to this problem generates incorrect
results because of python not working with very large numbers well in certain
situations.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns string representation of sum of list of numbers
# should work correctly with very large numbers
def addLongNumbers(numberList):

    # initialise string to store result
    largeSum = ''

    carry = 0
    digits = len(str(numberList[0]))

    # so we can iterate backwards from least  to most significant digit
    for digit in range(digits-1,-1,-1):
        digitTotal = carry

        # work out total of least significant digits added together
        for number in numberList:
            digitTotal += int(str(number)[digit])

        # add least significant digit to answer
        largeSum = str(digitTotal)[-1] + largeSum

        if len(str(digitTotal)) > 1:
            # set carry to every digit but least significant
            carry = int(str(digitTotal)[:-1])

        else:
            carry = 0


    if carry == 0:
        return largeSum
    
    return str(carry) + largeSum


# uses addLongNumbers() to repeatedly multiply up to n
# returns string representation of n!
def largeFactorial(n):
    answer = '1'
    for i in range(1, n):
        # since n * i  = n + n + ... + n (with i total terms)
        # effectively we are multiplying n! by (n+1) repeatedly
        answer = addLongNumbers([answer]*(i+1))
    return answer


print (f'The sum of the digits in the number 100! is {sum(int(digit) for digit in (largeFactorial(100)))}')
