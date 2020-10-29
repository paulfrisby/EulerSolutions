# ------------------------------------------------------------------------------
# Project Euler - Problem 037 - Truncatable primes
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=037
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
forwardTruncatable(number)
    while length(number) > 0 
        remove first digit
        if not prime
            return False
    return True

backwardTruncatable(number)
    while length(number) > 0 
        remove last digit
        if not prime
            return False
    return True

Generate primes using sieve of Eratosthenes
sum = 0
for each prime in list
    if forwardTruncatable(prime) and backwardTruncatable(prime)
    sum = sum + prime
        
print sum
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


# returns True only if every time you remove the first digit of the prime, it is still in the primeList
def forwardTruncatable(prime, primeList):

    # as single digit primes are not truncatable by definition
    if prime < 10:
        return False
    
    while len(str(prime)) > 1:
        prime = int(str(prime)[:-1])
        if primeList[prime] == 0:
            return False
    return True


# returns True only if every time you remove the last digit of the prime, it is still in the primeList
def backwardTruncatable(prime, primeList):

    # as single digit primes are not truncatable by definition
    if prime < 10:
        return False
    
    while len(str(prime)) > 1:
        prime = int(str(prime)[1:])
        if primeList[prime] == 0:
            return False
    return True


# creating a list where iff n is prime list[n] = n , otherwise list[n] = 0
primeSieve = primeSieve(1000000)

# creating a list of only the prime numbers
justPrimes = []
for number in primeSieve:
    if number != 0:
        justPrimes.append(number)
        
runningSum = 0
print('Left and right truncatable primes:')
for prime in justPrimes:
    if forwardTruncatable(prime, primeSieve) and backwardTruncatable(prime, primeSieve):
        print(prime)
        runningSum += prime

print('Total =', runningSum)
