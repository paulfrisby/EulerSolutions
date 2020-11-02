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
For an n by n spiral, we can see that:
- top right value = n^2
- top left value = n^2 - (n-1)
- bottom left value = n^2 - 2(n-1)
- bottom right value = n^2 - 3(n-1)

So in total, when we go from an n-2 by n-2 spiral to an n by n spiral, we add
4n^2 - 6n + 6 to the total

Let total = 1 (for 1 by 1 spiral)
for each odd value from 3 to 1001:
    total = total + 4n^2 - 6n + 6
print total
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

def spiralDiagSum(n):
    total = 1

    # iterating through every odd number up to, and including, n
    for i in range(3, n + 1, 2):
        total += 4*(i**2) - 6*i + 6
        
    return total

print (spiralDiagSum(1001))
