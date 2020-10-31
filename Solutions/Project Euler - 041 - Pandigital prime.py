# ------------------------------------------------------------------------------
# Project Euler - Problem 041 - Pandigital prime
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=041
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
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
generate list of primes under 10 digits in length, using Sieve of Eratosthenes

for each prime in list (from last to first):
    if prime is pandigital:
        print prime
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Optimisiations
# ------------------------------------------------------------------------------
"""
A number is divisible by 9 if its digits sum to a multiple of 9.

1+2+3+4+5+6+7+8+9 = 45 = 9 * 5
1+2+3+4+5+6+7+8   = 36 = 9 * 4

Therefore any 8 or 9 digit pandigital numbers will be divisible by 9, and thus,
not prime.

We only need to check primes up until 7,654,321 (the largest 7-digit pandigital
number)
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
            
    return primes


# where number has n digits
# returns true iff input number contains the digits 1 to n exactly once each
def nDigitPandigital(number):

    # number of digits number has
    n = len(str(number))

    # if it has more than 9 digits, at least 1 digit is repeated
    if n > 9:
        return False

    # checks if any digits are missing
    for i in range(1, n+1):
        if str(i) not in str(number):
            return False

    # if none of the other checks have triggered, the number must be pandigital
    return True


# generate list of primes up to & including largest 7 digit pandigital number
primes = primeSieve(7654321 + 1)

# iterate over primes backwards, so first pandigital prime is the largest
for prime in primes[::-1]:
    if nDigitPandigital(prime):
        print (f'{prime} is the largest n-digit pandigital prime')
        break
