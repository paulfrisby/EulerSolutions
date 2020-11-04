# ------------------------------------------------------------------------------
# Project Euler - Problem 049 - Prime permutations
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=049
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
generate all possible 4 digit permutation groups
for each group:
    find all possible arithmetic sequence triples
    for each triple:
        if all 3 are prime:
            print result
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# given a string, returns all unique permutations of characters of string
def permutations(string):

    # base case
    if len(string) == 1:
        return [string]

    perms = []

    # uses recursive approach to prepend each character to all possible
    # permutations of remaining characters
    for i in range(len(string)):
        char = string[i]
        reducedString = string[:i] + string[i+1:]
        laterPerms = permutations(reducedString)
        for perm in laterPerms:
            perms.append(char + perm)

    # removing duplicate permutations
    perms = list(set(perms))
    
    # puts permutations in ascending order
    perms.sort()
    
    return perms


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


# creating list of smallest possible 4 digits permuation within each group
# i.e. 1478 will be produced, but not 1487, 4817, or 8147
leastPerms = []
for i in range(10):
    for j in range(i,10):
        for k in range(j,10):
            for l in range(k,10):
                leastPerm = str(i) + str(j) + str(k) + str(l)
                leastPerms.append(leastPerm)

# creating a list of groups of 4-digit permutations of each other
# e.g. [4556, 4565, 4655, 5456, 5465, 5546, 5564, 5645, 5654, 6455, 6545, 6554]
# would be 1 list within the permGroups list
permGroups = []
for perm in leastPerms:
    permGroups.append(permutations(perm))
    
# removing permutations with a trailing 0
sanitisedPermGroups = []
for permGroup in permGroups:
    sanitised = []
    for perm in permGroup:
        if perm[0] != '0':
            sanitised.append(perm)

    # removing permutation groups with less than 3 permutations
    if len(sanitised) > 2:
        sanitisedPermGroups.append(sanitised)
        
permGroups = sanitisedPermGroups

found = 0

# used to check primality of permutations later
primes = primeSieve(10000)

# iterate though each group of permutations
for permGroup in permGroups:

    # we know from problem definition there are 2 results
    if found == 2:
        break

    # iterate through every combination of 1st / 2nd permutation
    for i in range(len(permGroup[:-2])):
        for j in range(i+1, len(permGroup[:-1])):
            perm1 = int(permGroup[i])
            perm2 = int(permGroup[j])

            # works out 3rd perm, assuming it follows arithmetic progressions
            difference = perm2 - perm1
            perm3 = perm2 + difference

            # checks if calculated 3rd perm actually exists in group
            if str(perm3) in permGroup:

                # checks if all 3 permutations are prime
                if perm1 in primes:
                    if perm2 in primes:
                        if perm3 in primes:
                            found += 1
                            print (f'{perm1}, {perm2}, & {perm3} are 4-digit permutations of one another, and are all prime')
