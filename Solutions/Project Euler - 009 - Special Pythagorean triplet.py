# ------------------------------------------------------------------------------
# Project Euler - Problem 009 - Special Pythagorean triplet
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=009
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns the first Pythagorean triple found where a+b+c = n
# if multiple triples exist, one with largest value of a found and returned
def pythagoreanTripleBySum(n):

    # since a<b<c, a is less than a third of total
    a = int(n / 3)

    # checks every combination of a,b,c where they total n and a<b<c is true
    # since a,b,c are natural numbers by problem definition, a must be positive
    while a > 0:

        # since b must be larger than a
        b = a + 1

        #since a + b + c = n
        c = n - a - b
        
        # since b<c by definition
        while b < c:

            # check if current values form a Pythagorean triple, returning if so
            if a**2 + b**2 == c**2:
                return [a, b, c]
            
            # incrementing b and decrementing c for next loop runthrough
            # a+b+c = n is still true since a is unchanged at this point,
            # and net changes to b+c is 0
            b += 1
            c -= 1

        # a is decremented if no triple is found with given value
        a -= 1

    # only runs if no Pythagorean triple with a+b+c = n exists
    return [False, False, False]

# assigning 3 items of returned list to 3 variables
a, b, c = pythagoreanTripleBySum(1000)

# using f-strings to print various info about answer
print (f'a = {a}, b = {b}, c = {c}')
print (f'{a}^2 + {b}^2 = {c}^2 = {c**2}')
print (f'a+b+c = {a}+{b}+{c} = 1000')
print (f'a*b*c = {a}*{b}*{c} = {a*b*c}')
