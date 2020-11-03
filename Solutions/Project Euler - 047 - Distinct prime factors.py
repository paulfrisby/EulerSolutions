# ------------------------------------------------------------------------------
# Project Euler - Problem 047 - Distinct prime factors
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=047
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
Generate a list of primes using sieve of eratosthenes

def primeFactorisation(n):
    i = 0
    factors = []
    while n > 0:
        if n evenly divides in to ith prime:
            add ith prime to factors
            n = n / ith prime
        else:
            i = i + 1
    return factors

n = 210 (2x3x5x7)
while true:
    if primeFactorisation(n) has 4 unique numbers:
        if pF(n+1), if pF(n+2), & pF(n+3) also have 4 unique numbers:
            print n
            break
    n = n + 1
"""
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Optimisation
# ------------------------------------------------------------------------------
"""
Original implementation of this was taking ~11.3s to run so I decided to try and
find a more efficient approach.

By slightly altering how the prime sieve works, we can automatically count how
many distinct factors each number has.

When a prime is being sieved out, instead of only marking multiples starting
from p^2 and incrementing by 2p, you can iterate over every multiple and
increment a counter for number of distinct factors. When finding the next prime,
just look for the next item in the list with 0 distinct factors so far.

This approach took ~0.145s to compute, about 75 times faster than the initial
approach.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

from time import time

# returns a list of primes under limit
# uses sieve of Eratosthenes method to generate efficiently
def primeSieve(limit):

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

    # removing multiples of odd primes    
    prime = 3
    while prime*prime < limit:

        # first multiple which needs to be removed is the square of prime
        # lesser multiples removed when multiples of lower primes sieved out
        # this is also why the p*p < limit evaluation is used for while loop
        mult = prime*prime

        # only odd multiples need to be removed, even numbers already sieved out
        # an even difference is applied to the mult so total value is still odd
        diff = 2*prime

        # setting value of every multiple of current prime to 0
        while mult < limit:
            primes[mult] = 0
            mult += diff

        # finding next prime in list, so that can be sieved out too    
        prime += 2
        while primes[prime] == 0:
            prime += 2

    # remove repeat values from list (i.e. all the extra 0s)
    primes = list(set(primes))
    primes.sort()
    
    # doesn't include 0th element as that is 0, not a prime
    return primes[1:]


# returns a list showing prime factorisation of n 
def primeFactorisation(n):
    i = 0
    factors = []
    while n > 1:
        if n % primes[i] == 0:
            factors.append(primes[i])
            n = int(n/primes[i])
        else:
            i += 1
    return factors


# returns the number of distinct prime factors n has
def distinctPrimeFactors(n):
    return len(set(primeFactorisation(n)))


# uses sieve to set number of distinct prime factors of each nuumber under limit
def distinctPrimeFactorSieve(limit):

    distinctFactors = [0]*limit
    
    # iterating over multiples of 2 
    prime = 2
    mult = prime
    while mult + 2 < limit:
        distinctFactors[mult] += 1
        mult += 2

    # incrementing multiples of odd primes    
    prime = 3
    while prime < limit:
        mult = prime

        # incrementing factor count for every multiple of current prime
        while mult < limit:
            distinctFactors[mult] += 1
            mult += prime

        # finding next prime in list, so that can be sieved out too    
        prime += 2
        while prime < limit and distinctFactors[prime] != 0:
            prime += 2

    return distinctFactors
    

start = time()
primes = primeSieve(500000)

# 2*3*5*7 = 210, 1st number with 4 distinct prime factors
n = 210
consecutive = 0
while True:
    if distinctPrimeFactors(n) == 4:
        consecutive += 1
    else:
        consecutive = 0
    if consecutive == 4:
        print (f'{n-3}, {n-2}, {n-1}, & {n} are the first four consecutive integers to have four distinct prime factors each.')
        break
    n += 1
end = time()

print (f'Time taken to compute:')
print (f'distinctPrimeFactors() - {end - start}s')

start = time()
factors = distinctPrimeFactorSieve(500000)

# 2*3*5*7 = 210, 1st number with 4 distinct prime factors
n = 210
while True:
    if factors[n:n+4] == [4,4,4,4]:
        print (f'{n}, {n+1}, {n+2}, & {n+3} are the first four consecutive integers to have four distinct prime factors each.')
        break
    n += 1
end = time()

print (f'distinctPrimeFactorSieve() - {end - start}s')
