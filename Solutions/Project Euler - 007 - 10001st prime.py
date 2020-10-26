# ------------------------------------------------------------------------------
# Project Euler - Problem 007 - 10001st prime
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=007
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Code optimisation / Speed comparison
# ------------------------------------------------------------------------------
"""
2 different methods of solving this problem are implemented here:

Method 1 - simply iterates through every odd integer after 2 and checks whether
it's evenly divisible by any odd integer less than or equal to square root of it
This is repeated until 10001st prime is found

Method 2 - Implements Sieve of Eratosthenes to generate a list of primes up
to a given limit, using an upper bound of approximation for nth prime so that it
is not generating too many list items. Once the he 10001st prime has been
reached during the generation of this, it is returned.

Source used to learn about this:
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

For current implementations, method 2 is ~3 times faster to find 10001st prime.

Method 2 has a larger advantage the larger n becomes:
~4 times faster to find 10,001st prime
~8 times faster to find 100,001st prime
~20 times faster to find 1,000,001st prime
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

from math import *
from time import time


# checks whether n is even divisble by 2 or any odd integer up to the square root of n
# to check whether n is prime or not
def isPrime(n):

    # since 1 is not prime by definition 
    if  n < 2:
        return False

    # since 2 is the only even prime
    elif n == 2:
        return True
    elif n%2 == 0:
        return False

    # checking divisiblilty by all potential odd factors
    else:
        for divisor in range(3, int(sqrt(n)) + 1, 2):
            if n%divisor == 0:
                return False
            
        return True


# iterates through every integer to check if it is prime, then returns nth positive result
def nthPrimeTrialDiv(n):
    prime = 0
    i = 0
    while i < n:
        prime += 1
        if isPrime(prime):
            i += 1
    return prime


# returns nth prime as soon as it is found during the creation of Sieve of Eratosthenes based prime list
def nthPrimeSieve(n):

    # upper bound of approximation for value of nth prime
    limit = int( n * log(n) + n * log(log(n)) )

    # establishing list of integers up to, but not including limit
    primes = []
    for i in range(limit):
        primes.append(i)

    # as 1 is defined as not prime, setting this element of list to 0
    primes[1] = 0
    
    # setting all numbers divisible by 2 to 0 (excluding 2 itself) 
    prime = 2
    mult = 2
    while mult + 2 < limit:
        mult += 2
        primes[mult] = 0

    # initialising a count of which prime we are currently sieving out, 3 is the 2nd prime number nad is what we are about to sieve out
    primeCount = 2

    # removing multiples of odd primes    
    prime = 3
    while primeCount < n:

        # the first multiple which needs to be removed is the square of prime in question
        # multiples less than this have already been removed when multiples of lower primes were sieved out
        # this is also why the p*p < limit evaluation is used for while loop
        mult = prime*prime

        # only odd multiples need to be removed, as even numbers have already been sieved out
        # therefore an even difference is applied to the mult such that the total value is still odd
        diff = 2*prime

        # setting value of every multiple of current prime to 0
        while mult < limit:
            primes[mult] = 0
            mult += diff

        # finding next prime in list, so that can be sieved out too    
        prime += 2
        while primes[prime] == 0:
            prime += 2

        # since new prime has now been found an we are going back to start of while loop, increment counter of which prime we're on    
        primeCount += 1
            
    return prime


print ("10001st prime:", nthPrimeSieve(10001))
print ("Time taken to generate:")

start0 = time()
nthPrimeTrialDiv(10001)
end0 = time()
print ("Trial Division method:", (end0 - start0), "seconds")

start1 = time()
nthPrimeSieve(10001)
end1 = time()
print ("Sieve of Eratosthenes method:", (end1 - start1), "seconds")
