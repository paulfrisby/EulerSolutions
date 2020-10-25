# ------------------------------------------------------------------------------
# Project Euler - Problem 003 - Largest prime factor
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=003
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

def largestPrimeFactor(number):

    # dealing with 2 separately as it is the only even prime number
    while number%2 == 0:

        # will only run if number is a power of 2, and thus has no higher prime factors
        if number == 2:
            return 2

        # divide by 2 if it is evenly divisble, so next factor can be found
        elif number % 2 == 0:
            number = number / 2

    
    prime = 3
    while number > prime:

        # divide by prime if it is evenly divisble by it, so next factor can be found
        if number % prime == 0:
            number = number / prime

        # Iterates to next possible factor to check. This won't always be a prime number,
        # but no none-prime numbers will divide the number evenly as all factors of that
        # nonprime have already been factored out earlier.
        else:
            prime = prime + 2
            
    return prime

print (largestPrimeFactor(600851475143))
