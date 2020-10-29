# ------------------------------------------------------------------------------
# Project Euler - Problem 016 - Power digit sum
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=016
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Discussion of approach
# ------------------------------------------------------------------------------
"""
This problem hinges on the fact that many programming languages do not deal with
very large numbers very well natively.

Even though the below below approaches are very simple and theoretically sound,
only sumOfDigitsString() works correctly. sumOfDigitsDivision() produces an
incorrect result for very large numbers.

Even sumOfDigitsString() is benefitting from python being able to store 2^1000
correctly at some level, which likely doesn't hold for all situations or
languages.

As such, I have also implemented a function to compute large powers using strings
only, and used a call to guarantee a correct string representation of 2^1000
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# works properly for given problem, although not certain if this will hold true
# for much larger numbers
def sumOfDigitsString(n):
    total = 0
    for digit in str(n):
        total += int(digit)

    return total


# works properly for smaller numbers, but incorrect result given for 2^1000 
def sumOfDigitsDivision(n):
    total = 0
    for i in range(len(str(n))):
        total += n%10
        n = int(n/10)

    return total


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


# returns string representation of n^power
# should work with very large results
def largePower(n, power):

    answer = '1'

    for step in range(int(power)):
        answer = addLongNumbers([answer]*int(n))

    return answer
         

print (f'The sum of the digits of 2^1000 is {sum(int(digit) for digit in (largePower(2, 1000)))}')
