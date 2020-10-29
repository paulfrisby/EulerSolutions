# ------------------------------------------------------------------------------
# Project Euler - Problem 004 - Largest palindrome product
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=004
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

def isPalindromic(n):
    return str(n) == str(n)[::-1]

def largestPalindromicProduct(digits, printcalc=""):
    
    # initialising x and y to largest possible 3 digit numbers
    x = 10**digits - 1
    y = 10**digits - 1

    # initialising variables to store largest palindromic product, and the factors used to produce it
    product = 0
    factx = 0
    facty = 0

    # checks all combination of x & y,
    # loop ends early if no possible multiple of factors could be larger than largest product already found.
    # iterates backwards towards 0 as we are looking for largest product,
    # ignoring smaller products without having to compute every single one is more efficient
    while y > 0 and y*(10**digits-1) > product:
        while x > 0 and x*y > product:
            if isPalindromic(x*y):
                product = x*y
                factx = x
                facty = y
            x -= 1
        y -= 1
        x = 10**digits - 1

    # prints out full calculation for result if optional argument included    
    if printcalc == "y":
        print (factx, "*", facty, "=", product)
        
    return product


largestPalindromicProduct(3, printcalc="y")
