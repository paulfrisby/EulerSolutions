# ------------------------------------------------------------------------------
# Project Euler - Problem 028 - Number spiral diagonals
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=028
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

[21] 22  23  24 [25]
 20 [ 7]  8 [ 9] 10
 19   6 [ 1]  2  11
 18 [ 5]  4 [ 3] 12
[17] 16  15  14 [13]

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
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

def spiralDiagSum(n):
    total = 1
    for i in range(int((n-1)/2)):
        total += 4 * ( ((2*i)+1)**2 ) + 10 * (2*(i+1))
    return total

print (spiralDiagSum(1001))
