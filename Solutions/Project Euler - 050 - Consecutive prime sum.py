# ------------------------------------------------------------------------------
# Project Euler - Problem 050 - Consecutive prime sum
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=050
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
generate list of primes below 1 million

longestsequence = 0
longestprime = 0

for each prime in list
    lowerbound = upperbound = 0
    primesequence = 0
    while upperbound < prime
    
        if sum(primes from lowerbound to upperbound) = prime
            sequencelength = upperbound - lowerbound + 1
            if sequencelength > primesequence
                primesequence = sequence length
            increment lowerbound and upperbound

        else if sum(primes from lowerbound to upperbound) < prime
            increment upperbound

        else if sum(primes from lowerbound to upperbound) > prime
            increment lowerbound

    if primesequence > longestsequence
        longestsequence = primesequence
        longestprime = prime

print prime, longest sequence
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

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


primes = primeSieve(1000000)

# using sequence given in problem definition
longestSequence = 21
longestPrime = 953

lowerBound = 0

while lowerBound + longestSequence < len(primes):

    # making initial sequence 1 longer than longest found so far
    # no need to find shorter sequences
    sequenceLength = longestSequence + 1
    upperBound = lowerBound + longestSequence
    sequenceSum = sum(primes[lowerBound:upperBound+1])
    
    while sequenceSum < 1000000:

        # since sequence is getting longer each time this runs, it will always
        # be longest sequence found so far
        if sequenceSum in primes:
            longestPrime = sequenceSum
            longestSequence = sequenceLength


        # updating values for next loop runthrough
        upperBound += 1
        sequenceLength += 1
        sequenceSum += primes[upperBound]

    lowerBound += 1
        
print (f'{longestPrime} can be written as the sum of {longestSequence} consecutive primes')
