# ------------------------------------------------------------------------------
# Project Euler - Problem 032 - Pandigital products
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=032
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Plan / Pseudocode
# ------------------------------------------------------------------------------
"""
Since 2 2-digit numbers or a 3/1-digit number multiplied with each other
can never exceed 4 digits, the calculation would only feature 8 digits maximum,
and thus couldn't be pandigital.

Since 2 3-digit numbers or  4/2-digit numbers or 5/1-digit numbers multiplied
by each would always be at least 5 digits, the calculation would feature 11
digits minimum, and thus couldn't be pandigital.

Therefore the two numbers being multiplied together must have exactly 5 digits
between them, and they must produce a 4 digit number when multiplied.

Let i * j = i*j be a product, where i > j, and 999 < i*j < 10,000

products = []

for i from 100 to 5000:
    for j from 2 to 99:
        if (string(i) + string(j) + string(i*j)) is pandigital:
            products = products + i*j

print sum of unique numbers in products list         
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns whether an input number or string is 1 to 9 pandigital
def isPandigital(n):
    n = str(n)
    if len(n) != 9:
        return False
    for num in '123456789':
        if num not in n:
            return False           
    return True


print ('The following identities containing multiplicand, multiplier, & product are 1 to 9 pandigital:')

# work out products for all i*j where i > j, and 999 < i*j < 10000
# prints out calculation and stores product if it is pandigital
pandigitalProducts = []
for i in range(100, 5000):
    for j in range(int(1000/i), 100):
        if i*j > 9999:
            break
        elif isPandigital(str(i) + str(j) + str(i*j)):
            print (f'{i} * {j} = {i*j}')
            pandigitalProducts.append(i*j)

# sum(set()) is used to only sum the unique products
# a set in python is unsorted and can't have repeated elements
print (f'The sum of the unique products is {sum(set(pandigitalProducts))}')
