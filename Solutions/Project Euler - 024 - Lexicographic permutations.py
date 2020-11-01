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
to find nth permutation of x objects

n = n-1

for each position in permutation:
    binsize = x! / x
    i = int(n / binsize)
    let the ith ordered object be in this position
    delete ith object from objects

    x = x - 1
    n = n % binsize


For example, in the case of finding 4th permutation of 0, 1 & 2:

(n = 4, x = 3, digits = [0,1,2])

n = n - 1 = 4 - 1 = 3

position 1:
    binsize = x! / x = 3! / 3 = 6 / 3 = 2
    i = int(n/binsize) = int(3/2) = 1
    position 1 is digits[1] = 1

    remaining digits = [0,2]
    x = x - 1 = 3 - 1 = 2
    n = n % binsize = 3 % 2 = 1

position 2:
    binsize = x! / x = 2! / 2 = 2 / 2 = 1
    i = int(n/binsize) = int(1/1) = 1
    position 2 is digits[1] = 2

    remaining digits = [0]
    x = x - 1 = 2 - 1 = 1
    n = n % binsize = 1 % 1 = 0

position 3:
    since binsize is now 0, we only have 1 option left
    position 3 is 0

The 4th permutation of 0, 1 & 2 is '120'
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns n!
def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial


# returns nth permutation (ordered lexicographically) of elements in objects
def perm(objects, n):

    length = len(objects)

    # error catching
    # there are exactly x! possible permutations, where objects has x elements
    if factorial(length) < n:
        return f'There are not {n} possible permutations of the objects in {objects}'
    
    # in case objects are not passed already in lexicographic order
    objects.sort()
    permutation = ''
    n -= 1
    
    while length > 1:

        # amount of permutations with each object in next position
        binsize = factorial(length) / length
        
        # find out which object is next by finding out which bin n falls in
        permutation += str(objects[int(n/binsize)])

        # this object can not be reused, so delete it
        del objects[int(n/binsize)]

        # update values for next calculation
        n = n % binsize
        length -= 1

    # add last remaining object to permutation    
    permutation += str(objects[0])
    return permutation


print (f'The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 & 9 is {perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000)}')
