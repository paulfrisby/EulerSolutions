# ------------------------------------------------------------------------------
# Project Euler - Problem 036 - Template File
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=036
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The decimal number, 585 = 1001001001(binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
toBinary(decimal):
    binary = ''
    while decimal > 0:
        if decimal / 2 has a remainder of 1:
            binary = '1' + binary
        else:
            binary = '0' + binary
        decimal = roundDown(decimal / 2)
    return binary

isPalindromic(number):
    numberString = string(number)
    reverseNumberString = reverse(numberString)
    if numberString == reverseNumberString:
        return True
    else:
        return False

runningSum = 0
for each number below 1000000:
    convert number to binary
    if (decimal number is palindromic) and (binary number is palindromic):
        sum = sum + number

print runningSum
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns a string of the binary representation of input number
def toBinary(decimal):
    binary = ''
    while decimal > 0:
        if decimal%2 == 1:
            binary = '1' + binary # prepends number as we are working from right to left binary digits
        else:
            binary = '0' + binary
        decimal = int(decimal/2)
    return binary


def isPalindromic(number):
    number = str(number) # cast to string so string reverse using a slice can be done

    # number is not palindromic if last digit is 0
    if number[-1] == '0':
        return False

    return (number == number[::-1])


runningSum = 0
for decimal in range(1000000):
    binary = toBinary(decimal)
    if isPalindromic(decimal) and isPalindromic(binary):
        runningSum += decimal
print (runningSum)
