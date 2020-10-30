# ------------------------------------------------------------------------------
# Project Euler - Problem 040 - Champernowne's constant
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=040
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
stringChampernownes(n):
    constant = '.'
    integer = '1'
    while length of constant <= n:
        constant += string(integer)
    return constant


constant = stringChampernownes(1,000,000)

print (constant[1] * constant[10] * constant[100] * constant[1,000] *
       constant[10,000] * constant[100,000] * constant[1,000,000])
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Optimisation
# ------------------------------------------------------------------------------
"""
While the initial unoptimised algorithm to solve this completes in ~0.052s, it
quickly increases in time taken as the last digit in multiplication gets later.

For instance, it takes ~2.9s to run when adding 10,000,000th digit to end of
list of products, and ~250s when adding 100,000,000th digit.

After some consideration I was able to produce a function which returns the nth
digit of Champernowne's constant in roughly constant time, regardless of how
large the position you ask for is.

For instance when multiplying powers of 10 up to 100,000,000, the optimised
solution reports taking 0.0s to complete according to the time() function, as
opposed to ~250s it took the unoptimised approach to compute.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

from time import time


# returns string representation of Champernowne's constant to n decimal places
def stringChampernownes(n):
    constant = '.'
    integer = 1
    while len(constant) <= n:
        constant = constant + str(integer)
        integer += 1
    return constant[:n+1]


# returns multiple of digits of Champernowne's constant at given positions
def unoptimisedChampernownesProductOfPositions(positions):
    constant = stringChampernownes(max(positions))

    # finds vale of needed digits and multiplies them together
    answer = 1
    for position in positions:
        answer = answer * int(constant[position])
        
    return answer


# returns the position in string of the first digit of n
def champernownePositionFromNumber(n):
    digits = len(str(n))
    return digits*n - int('1' * digits) + 1


# returns multiple of digits of Champernowne's constant passed in positions list
def champernownesDigitFromPosition(position):

    # digitBounds[n] stores first & last positions in Champernowne's
    # constant that n-digit numbers occupy
    # e.g. 2-digit numbers start in the 10th position and end in the 189th
    digitBounds = [[0, 0],
                   [1, 9],
                   [10, 189],
                   [190, 2889],
                   [2890, 38889],
                   [38890, 488889],
                   [488890, 5888889],
                   [5888890, 68888889],
                   [68888890, 788888889],
                   [788888890, 8888888889],
                   [8888888890, 98888888889],
                   [98888888890, 1088888888889],
                   [1088888888890, 11888888888889],
                   [11888888888890, 128888888888889],
                   [128888888888890, 1388888888888889],
                   [1388888888888890, 14888888888888889],
                   [14888888888888890, 158888888888888889],
                   [158888888888888890, 1688888888888888889],
                   [1688888888888888890, 17888888888888888889],
                   [17888888888888888890, 188888888888888888889],
                   [188888888888888888890, 1988888888888888888889],]

    # if needed, updating digitBounds until position is included within one of them
    # bounds already stored for up to 20 digits
    digits = len(digitBounds)
    while digitBounds[-1][1] < position:
        lowerBound = int(str(digits - 2) + '8'*(digits - 3) + '90')
        upperBound = int(str(digits - 1) + '8'*(digits - 1) + '9')
        digitBounds.append([lowerBound, upperBound])
        digits += 1
        
    # find out which bin it falls in / how many digits number at this position has
    for i in range(1,len(digitBounds)):
        if digitBounds[i][1] >= position:
            positionDigits = i
            lowerBound = digitBounds[i][0]
            upperBound = digitBounds[i][1]
            break

    # e.g. the first 2-digit number is 10
    firstNDigitNum = 10**(positionDigits - 1)

    # e.g. there are 90 2-digit numbers
    totalNDigitNums = 10**(positionDigits) - 10**(positionDigits - 1)

    # how far along the n-digit number interval given position is at
    intervalPosition = (position -  lowerBound) / (upperBound - lowerBound + 1)
    
    # find out which number / digit of that number is at this position
    number = int(firstNDigitNum + totalNDigitNums * intervalPosition)

    # for an n-digit number, the fractional part of:
    # (firstNDigitNumber + totalNDigitNums * intervalPosition)
    # will be equal to i/n
    # where i is the ith digit of the number (starting counting from 0)
    # so we find the remainder when divinding by 1, then multiply by n, to get i
    digitOfNumber = int((firstNDigitNum + totalNDigitNums * intervalPosition) %1 * positionDigits)
    
    return int(str(number)[digitOfNumber])


# returns product of digits of Champernowne's constant passed in positions list
def champernownesProductOfPositions(positions):
    totalProduct = 1
    for position in positions:
        totalProduct = totalProduct * champernownesDigitFromPosition(position)
    return totalProduct


# runs a set of inputs on all 3 implementations and prints results / time took
def timeCompare(argumentList):
    for argument in argumentList:

        start = time()
        answer = champernownesProductOfPositions(argument)
        end = time()        
        print (f'Product of the digits at positions {argument} is {answer}')
        print (f'Time taken to compute:')
        print (f'champernownesProductOfPositions() - {end - start}s')
        

        start = time()
        answer = unoptimisedChampernownesProductOfPositions(argument)
        end = time()
        print (f'unoptimisedChampernownesProductOfPositions() - {end - start}s')
        print ('\n')


timeCompare([[1, 10, 100],
             [1, 10, 100, 1000],
             [1, 10, 100, 1000, 10000],
             [1, 10, 100, 1000, 10000, 100000],
             [1, 10, 100, 1000, 10000, 100000, 1000000],
             [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],
             [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]])
