# ------------------------------------------------------------------------------
# Project Euler - Problem 027 - Quadratic primes
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=027
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 <= n <= 39.

However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and
certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values 0 <= n <= 79.

The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
exhaustive check approach

try every possible value of a & b
for each see what number of consecutive primes it produces
if it is greater than largest chain so far:
    store value of a, b, a*b, & length of chain
return a*b

3,999,999 checks will need to be performed in total (1999 x 2001)
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

from math import *


# returns True iff n is prime
def isPrime(n):
    if  n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for divisor in range(3, int(sqrt(n)) + 1, 2):
            if n%divisor == 0:
                return False
        return True


# returns how many primes in a row the formula n^2 + an + b generates
def consecPrimes(a, b):
    count = 0
    while True:
        if isPrime(count*count + a*count + b):
            count += 1
        else:
            return count
    

largestChain = 0
abProd = 0

# iterate through all possible combinations of a,b
for a in range (-999,1000):
    for b in range(-1000,1001):
        if consecPrimes(a, b) > largestChain:
            largestChain = consecPrimes(a, b)
            abProd = a*b
            bestA = a
            bestB = b

print (f'n^2 + ({bestA})n + ({bestB}) generates {largestChain} consecutive primes starting from n = 0, a * b = {abProd}')
