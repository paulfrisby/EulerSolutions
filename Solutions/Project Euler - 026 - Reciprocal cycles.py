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

def digits(n):
    return len(str(n))


def decExpansion(n):
    div = 10 ** digits(n - 1)
    dec = []
    for j in range(digits(n - 1) - 1):
        dec += [[0, 10**(j+1)]]
    if div % n == 0:
        dec.append([int(div/n), 0])
        return dec
    dec += [[int(div/n), div % n]]
    while True:
        dec += [[int(dec[-1][1] * 10 / n), dec[-1][1] * 10 % n]]
        if dec[-1][1] == 0 and len(dec) > 1:
            return dec
        for i in range(len(dec) - 1):
            if dec[i][0] == dec[-1][0] and dec[i][1] == dec[-1][1]:
                return dec


# if 1/n has a repeating decimal this returns the length in digits of the
# recurring cycle, otherwise returns 0
def repeatDigits(n):
    dec = decExpansion(n)
    for i in range(len(dec) - 1):
        if dec[i][0] == dec[-1][0] and dec[i][1] == dec[-1][1]:
            return len(dec) - 1 - i
    return 0


# returns a string representation of decimal of 1/n
def decStr(n):
    decstr = '0.'
    dec = decExpansion(n)

    # non repeating decimal
    if dec[-1][-1] == 0:
        for i in range(len(dec)):
            decstr += str(dec[i][0])

    # repeating decimal       
    else: 
        for i in range(len(dec) - 1):
            if dec[i][0] == dec[-1][0] and dec[i][1] == dec[-1][1]:
                decstr += '('
            decstr += str(dec[i][0])
        decstr += ')'
            
    return decstr


h=0
for i in range (1,1000,2):
    j = repeatDigits(i)
    if j>h:
        h=j
        longestN=i

print (f'The longest recurring decimal in a fraction of the form 1/n is in 1/{longestN}:')
print (f'1/{longestN} = {decStr(longestN)}')
