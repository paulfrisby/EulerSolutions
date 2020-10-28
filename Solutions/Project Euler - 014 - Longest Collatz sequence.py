# ------------------------------------------------------------------------------
# Project Euler - Problem 014 - Longest Collatz sequence
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=014
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Time comparison
# ------------------------------------------------------------------------------
"""
After completing first implementation of code to solve this problem, I noticed
it was taking quite a long time to run. After some consideration I realised that
if we store the sequence length for each starting point, at any point where we
get to below our starting point on a subsequent calculation, we can just add the
length of the previous result to however long our sequence currently is to get
an answer.

Further optimisations may include storing the results of any highpoints reached
along the way also. e.g. For the example sequence given in the problem
definition we can already see the sequence length starting from 40 would be 9.

Below is a comparison of the time taken to compute the longest sequence below a
variety of starting points using both functions. Times given to 2 significant
figures of accuracy.

   Limit      Answer(start/length)   longestCollatz()  optimisedCollatz()
-----------  ----------------------  ----------------  ------------------
      1,000         871 / 179 terms           0.0065s             0.0097s                   
      5,000       3,711 / 238 terms           0.040s              0.0050s
     25,000      23,529 / 282 terms           0.24s               0.030s
    100,000      77,031 / 351 terms           1.1s                0.11s                 
    250,000     230,631 / 443 terms           3.0s                0.24s        
  1,000,000     837,799 / 525 terms          13s                  0.77s
  5,000,000   3,732,423 / 597 terms          75s                  3.9s
 25,000,000  15,733,191 / 705 terms         420s                 20s    
-----------  ----------------------  ----------------  ------------------

We can see from this that while times are acceptable at a lower limit, and even
faster at very low limits, the time it takes for longestCollatz() to compute
quickly blows up as the limit increases.

For the limit of 1,000,000, given in the problem definition, the optimised
algorithm is ~17 times quicker than the unoptimised one.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

from time import time

# returns number of terms in the Collatz sequence starting with n
def collatzLength(n):
    length = 1
    while n != 1:

        # n is odd
        if n%2:
            n = 3*n + 1

        # n is even
        else:
            n = int(n/2)
            
        length += 1

    return length

# iterates through every starting point up to limit
# and returns one with largest sequence length
def longestCollatz(limit):
    longestSequence = 0
    longestN = 0

    for n in range(1, limit):
        if collatzLength(n) > longestSequence:
            longestSequence = collatzLength(n)
            longestN = n

    return [longestN, longestSequence]


# Collatz sequence is only followed until we reach a value below starting point
# then we can lookup result calculated from earlier loop to calculate length of
# this sequence, without having to go all the way to the sequence end
def optimisedCollatz(limit):

    # sequenceLengths[n] = length of Collatz sequence starting at n
    # initialising each value to 0 until it has been calculated
    sequenceLengths = [0]*limit

    # base case initialised
    sequenceLengths[1] = 1

    longestSequence = 1
    longestN = 1

    for start in range(2,limit):
        n = start
        length = 0

        while True:
            
            # if answer already known for n, we can end loop
            if n < limit and sequenceLengths[n] != 0:
                sequenceLengths[start] = sequenceLengths[n] + length

                # check to see if this is longest sequence yet
                if sequenceLengths[start] > longestSequence:
                    longestSequence = sequenceLengths[start]
                    longestN = start
                break

            # n is odd
            if n%2:
                n = 3*n + 1

            # n is even
            else:
                n = int(n/2)
            
            length += 1

    return [longestN, longestSequence]


# displays time taken to compute sum of primes below limit using 2 methods 
def collatzTimeCompare(limit):
    
    start = time()
    n, length = optimisedCollatz(limit)
    print (f'The Collatz sequence starting with {n} has {length} terms')
    print (f'This is the longest chain starting under {limit}')
    end = time()
    
    print (f'Time taken to compute:')
    print (f'optimisedCollatz({limit}) - {end - start} seconds')

    start = time()
    n, length = longestCollatz(limit)
    end = time()
    print (f'longestCollatz({limit}) - {end - start} seconds')


collatzTimeCompare(1000000)
