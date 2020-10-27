# ------------------------------------------------------------------------------
# Project Euler - Problem 038 - Pandigital multiples
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=038
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9
and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
- Since n has to be at least 2, the integer used to produce the product can not
exceed 4 digits in length, as then the concatenated product would exceed 9

- n can also not exceed 9 for the same reason

- more generally n * len(integer) must not exceed 9

largestPandigital = 0

for n from 2-9:
    let integer = 1
    while n * length(integer) <= 9:
        concatenatedProduct = string(integer)
        for i from 2 to n:
            concatenatedProduct = concatenatedProduct + string(i*integer)
        if (concatenatedProduct is pandigital and larger than largestPandigital):
            largestPandigital = concatenatedProduct
        increment integer
        
print largestPandigital 
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns true iff input number contains the digits 1 to 9 exactly once each
def isPandigital(number):

    # number cast to a string for easier comparisons later
    # this line is redundant in cases where a string argument is input
    number = str(number)

    # if number has less than 9 digits it isn't pandigital
    # if it has more than 9 digits, at least 1 digit is repeated
    if len(number) != 9:
        return False

    # checks if any digits are missing
    for digit in '123456789':
        if digit not in number:
            return False

    # if none of the other checks have triggered, the number must be pandigital
    return True


largestPandigital = 0

for n in range(2,10):
    integer = 1

    # checks to see if result will be too large, so we can move to next value of n
    while n * len(str(integer)) <= 9:
        concatenatedProduct = ''
        
        # actual computation of concatenated product
        for i in range(1,n+1):
            concatenatedProduct += str(i*integer)

        # stores answer/products if it's pandigital and larger than largest one already found  
        if isPandigital(concatenatedProduct) and int(concatenatedProduct) > largestPandigital:
            largestPandigital = int(concatenatedProduct)
            largestN = n
            largestInteger = integer

        integer += 1

print (f'Concatenation of products of {largestInteger} * (1,...,{largestN}) = \'{largestPandigital}\'')
