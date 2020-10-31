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

from math import *

# exhaustive check approach

# try every possible value of a & b
# for each see what number of consecutive primes it produces
# if it is greater than largest so far update variable
# return value

# use prime check function
# potentially use sieve of Eratosthenes and check against this instead

# 3,996,001 checks will need to be performed (1999 x 1999)
# improvements could be made with check that eliminates a,b combos earlier

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

def consecPrimes(a, b, count = 0):
    if isPrime(count*count + a*count + b):
        return consecPrimes(a, b, count + 1)
    return count
    

largest = 0
abprod = 0

for i in range (1000):
    for j in range(1000):
        if consecPrimes(i, j) > largest:
            largest = consecPrimes(i, j)
            abprod = i*j
            a = i
            b = j
        if consecPrimes(i*-1, j) > largest:
            largest = consecPrimes(i*-1, j)
            abprod = i*j*-1
            a = -i
            b = j
        if consecPrimes(i, j*-1) > largest:
            largest = consecPrimes(i, j*-1)
            abprod = i*j*-1
            a = i
            b = -j
        if consecPrimes(i*-1, j*-1) > largest:
            largest = consecPrimes(i*-1, j*-1)
            abprod = i*j
            a = -i
            b = -j
print (f'n^2 + {a}n + {b} generates {largest} consecutive primes starting from n = 0, a * b = {abprod}')
