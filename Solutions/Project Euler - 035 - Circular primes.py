# ------------------------------------------------------------------------------
# Project Euler - Problem 035 - Circular primes
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=035
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
generate array of primes below 1,000,000 using sieve of Eratosthenes

for each prime in array of primes:
    check if its rotations are also present
        if not, remove it and any present rotations from array

remove zeroed out entries from array
check size of array after purge of non circular primes for result
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns a list where if n is a prime, list[n] = n, otherwise list[n] = 0
# uses sieve of Eratosthenes method to generate efficiently
# largely reused code from project euler problem 7
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
            
    return primes


# returns list of all rotations of an integer
# e.g. rotations of 386 are 386, 638, & 863
def integerRotations(n):

    # initialising empty array for results
    rotations = []

    # an integer has an equalamount of rotations and digits, so this runs once per digit of n
    for i in range(len(str(n))):

        # adds n to results array
        rotations.append(n)

        # removes last digit from n and puts it before other digits
        n = int(str(n%10) + str(int(n/10)))
        
    return rotations


# returns a list where if n is a circular prime number, list[n] = n, otherwise list[n] = 0
def circPrimeSieve(limit):

    # to find all circular primes below 200 you need all the primes up to ~1,000
    # e.g. a rotation of 199 is 991, which needs to be checked for primeness
    newLimit = pow(10, len(str(limit-1)))
    circPrimes = primeSieve(newLimit)

    # starting at 11 as all single digit primes are circular by default
    prime = 11
    
    while prime < limit:
        
        #no prime number with a 0 as any digit can be circular as 1 or more rotation will end in 0, and thus be a multiple of 10
        hasZero = False
        primeZero = prime

        # checks whether last digit is 0, then truncates last digit to recheck next digit, repeatedly
        while primeZero>0:
            if primeZero%10 == 0:
                hasZero = True
                break
            primeZero = int(primeZero/10)

        # if prime has a 0 digit
        if hasZero:
            circPrimes[prime] = 0

        # if no 0 digit present in prime
        else:
            primeRotations = integerRotations(prime)
            # checks whether each rotation is prime, if not, removes all other rotations from results
            for rotation in primeRotations:
                if circPrimes[rotation] == 0:
                    for nonCircPrime in primeRotations:
                        circPrimes[nonCircPrime] = 0
                    break # as no need to check other rotations once one has been found to be non-prime
                    
        # finds the next prime left in list to check
        prime += 2
        while prime < limit and circPrimes[prime] == 0:
            prime += 2

    # trims results to respect limit in original argument
    return circPrimes[:limit]


def nonZero(n):
    if n == 0:
        return False
    else:
        return True
    
# filters out all 0s from sieved list of circular primes so we can see exactly how many there are
print(f'In total, there are {len(list(filter(nonZero, circPrimeSieve(1000000))))} circular primes below one million, they are:')
print(list(filter(nonZero, circPrimeSieve(1000000))))
