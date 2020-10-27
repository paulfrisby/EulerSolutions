# ------------------------------------------------------------------------------
# Project Euler - Problem 010 - Summation of primes
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=010
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
sum all primes below a limit (based on Sieve of Eratosthenes):
    generate list of numbers up to limit
    set list[1] = 0
    let prime = 2
    until prime > square root of limit
        for every multiple of prime
            set list[multiple] = 0
        set prime to next non-zero element of list
    sum resulting list
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Time comparison
# ------------------------------------------------------------------------------
"""
Similar to earlier problems I have implemented and timed an efficient approach
and a much more naive approach. To solve the exact given problem the efficient
approach is roughly 7 times faster (~0.5s vs ~3.5s).

Here I include the time it took to run for various limits to give a better idea
of efficiency difference. (time given to 2 significant figures of precision)

   Limit            Answer         Sieve of Eratosthenes  Trial Division
-----------  --------------------  ---------------------  --------------
      1,000                76,127                0.0030s         0.0010s
     10,000             5,736,396                0.0060s         0.0040s
    100,000           454,396,537                0.024s          0.067s
  1,000,000        37,550,402,023                0.24s           1.5s
  2,000,000       142,913,828,922                0.48s           3.8s
 10,000,000     3,203,324,994,356                2.4s           36s
100,000,000   279,209,790,387,276               25s            900s
-----------  --------------------  ---------------------  --------------

As can be seen from this table, Trial Division is faster until a limit of around
10,000, but it quickly falls behind as the limit increases, as the time it takes
to complete grows exponentially. The time it takes for the Sieve of Eratosthenes
method to complete seems to grow at the same rate as the limit in these tests. 
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

from math import *
from time import time


def sumOfPrimesSieve(limit):

    primes = [] 
    for i in range(limit):
        primes.append(i)
    
    # filters out all multiples of factor from parent functions primes list
    def sieveFactor(factor):

        # first multiple that needs to be removed is factor^2
        # all smaller multiples have smaller prime factor & are removed already
        mult = factor**2

        # once even numbers factored out, only every 2nd multiple needs sieved
        if factor == 2:
            diff = factor
        else:
            diff = factor*2
    
        
        # all remaining multiples of factor sieved out
        while mult < (len(primes)):
            primes[mult] = 0
            mult += diff

        
    # as 1 is non-prime by definition
    primes[1] = 0
    
    # sieve out non-prime even numbers
    sieveFactor(2)


    prime = 3

    # since we only need primes strictly below limit prime < sqrt(limit) is sufficient
    # prime <= sqrt(limit) would be necessary when the limit was included,
    # to catch the case where the limit is exactly the square of a prime
    while prime < sqrt(limit):
        sieveFactor(prime)

        # find next prime number to factor out in next loop runthrough
        prime += 2
        while primes[prime] == 0:
            prime += 2
            
    return sum(primes) 


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


# uses trial division to sum all primes below a limit
def sumOfPrimesTrialDiv(limit):

    # if limit is 2 or lower, there are no primes to sum
    if limit < 3:
        return 0
    
    else:
        
        # sum of primes below 3
        primeSum = 2
        
        prime = 3

        # checks all even numbers from 3 onwards for primality
        while prime < limit:
            if isPrime(prime):

                # add prime to sum
                primeSum += prime
                
            prime += 2
            
        return primeSum


# displays time taken to compute sum of primes below limit using 2 methods 
def primeTimeCompare(limit):
    
    start = time()
    print (f'Sum of primes below {limit} = {sumOfPrimesSieve(limit)}')
    end = time()
    
    print (f'Time taken to compute:')
    print (f'Sieve of Eratosthenes - {end - start} seconds')

    start = time()
    sumOfPrimesTrialDiv(limit)
    end = time()
    print (f'Trial Division - {end - start} seconds')


primeTimeCompare(2000000)
