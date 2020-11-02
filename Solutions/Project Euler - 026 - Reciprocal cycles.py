# ------------------------------------------------------------------------------
# Project Euler - Problem 026 - Reciprocal cycles
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=026
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2	 = 	0.5
    1/3	 = 	0.(3)
    1/4	 = 	0.25
    1/5	 = 	0.2
    1/6	 = 	0.1(6)
    1/7	 = 	0.(142857)
    1/8	 = 	0.125
    1/9	 = 	0.(1)
    1/10 = 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns a list of tuples with decimal digit / remainder for each digit of
# decimal expansion of 1/n
def decimalExpansion(divisor):
    remainder = 1
    decimal = []
    while True:
        dividend = 10*remainder
        quotient = int(dividend / divisor)
        remainder = int(dividend % divisor)
        decimal.append([quotient, remainder])

        # no remainder means the decimal does not have a repeating cycle
        # and we have fully computed it
        if remainder == 0:
            return decimal
        
        # if we have repeat remainder, we are now in the 1st digit of 2nd cycle 
        if decimal[-1] in decimal[:-1]:
            return decimal


# if 1/n has a repeating decimal this returns the length in digits of the
# recurring cycle, otherwise returns 0
def repeatDigits(n):
    decimal = decimalExpansion(n)

    # non repeating decimal
    if decimal[-1][-1] == 0:
        return 0
    
    # checks if position in decimal has same remainder as last position
    for i in range(len(decimal) - 1):
        if decimal[i] == decimal[-1]:
            return len(decimal) - 1 - i


# returns a string representation of decimal of 1/n
def decimalString(n):
    string = '0.'
    decimal = decimalExpansion(n)

    # non repeating decimal
    if decimal[-1][-1] == 0:
        for i in range(len(decimal)):
            string += str(decimal[i][0])

    # repeating decimal       
    else:

        # last element of list is 1st repeated digit, no need to add this
        # hence only iterating up to penultimate list element
        for i in range(len(decimal) - 1):

            # prepending parenthesis if this element is start of repeating cycle
            if decimal[i] == decimal[-1]:
                string += '('

            string += str(decimal[i][0])
        string += ')'
            
    return string


longestRepeat = 0
for i in range (1,1000):
    repeat = repeatDigits(i)
    if repeat > longestRepeat:
        longestRepeat = repeat
        longestN = i

print (f'The longest recurring decimal in a fraction of the form 1/n is in 1/{longestN}:')
print (f'1/{longestN} = {decimalString(longestN)}')
