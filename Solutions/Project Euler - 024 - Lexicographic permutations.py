# ------------------------------------------------------------------------------
# Project Euler - Problem 024 - Lexicographic permutations
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=024
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

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

def factorial(n):
    f = n
    for i in range(1, n):
        f = f * i
    return f

# returns nth permutation (ordered lexicographically) of elements in objects
def perm(objects, n):
    objects.sort()
    p = ''
    n -= 1
    x = len(objects)
    while x > 1:
        tot = factorial(x) / x 
        p += str(objects[int(n/tot)])
        del objects[int(n/tot)]
        n = n % tot
        x -= 1
    p += str(objects[0])
    return p

print (perm([0, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1000000))
