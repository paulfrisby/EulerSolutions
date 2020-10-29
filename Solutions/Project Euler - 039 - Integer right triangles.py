# ------------------------------------------------------------------------------
# Project Euler - Problem 039 - Integer right triangles
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=039
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Plan / Pseudocode
# ------------------------------------------------------------------------------
"""
Problem 9 involved finding the only Pythagorean triplet where perimeter = 1000

Let a,b,c and c be the sides of a right angled triangle, where c is hypotenuse,
and if a & b are not equal, let a be the shorter side, therefore a <= b < c

Refactor code from problem 9 to increment a counter when a triplet is found,
instead of immediately returning it, so that it can return the total number of
valid triplets for a given perimeter.

let a,b,c be a Pythagorean triplet with perimeter p

2a,2b,2c will also form a triplet with perimeter 2p

thus, perimeter 2p will have at least as many triplets as perimeter p

therefore we don't need to check below half of the perimeter limit, as every
perimeter in the lower half will have a counterpart in the upper half with at
least as many triplets.

max = 0
maxPerimeter = 0
For perimeter from 500 to 1000
    if pythagoreanTriplets(perimeter) > max
        max = pythagoreanTriplets(perimeter)
        maxPerimeter = perimeter

print (maxPerimeter)
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Optimised solution / time comparison
# ------------------------------------------------------------------------------
"""
Even though I had already implemented some optimisations in original solution
(e.g. only checking perimeter values greater than or equal to half of the limit)
it was taking over 20 seconds to computer the answer.

After some further consideration I came up with a more efficient approach.

Instead of working out triplets one perimeter length at a time, you can iterate
through every possible integer combination of a,b and for each, check if c is
also integral.

If so, we work out the perimeter and increment a counter for that perimeter

Once all combinations of a,b have been checked, simply check with perimeter has
the most solutions.

Further information on the specifics can be seen in inline comments.

Below is a comparison of the time taken using both functions for a variety of
limits. Times given to 2 significant figures of accuracy.

 Limit   Answer(perimeter/solutions)  original solution  optimised solution
-------  ---------------------------  -----------------  ------------------
    100            60  /   2                    0.035 s            0.0020 s                       
    250           240  /   4                    0.37  s            0.0030 s
  1,000           840  /   8                   24     s            0.047  s
  2,500         1,680  /  10                  390     s            0.31   s
 10,000         9,240  /  20                 N/A                   4.9    s
 25,000        18,480  /  25                 N/A                  31      s
-------  ---------------------------  -----------------  ------------------

While the compute time for the optimised solution still grows quite quickly as
the limit grows, it is a lot faster at every tested limit compared to original
solution. For the limit of 1,000, the optimised solution is ~500 times faster.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

from math import sqrt
from time import time


# returns number of Pythagorean triples that exist for given integer perimeter
def pythagoreanTripletsByPerimeter(perimeter):

    # to track result
    totalTriplets = 0

    # setup for 1st runthrough of loop
    a = 1
    b = 1
    c = perimeter - 2

    while a*a + b*b <= c*c:
        
        # each time this loop runs, b increases and c decreases
        # thus if a^2 + b^2 > c^2 we don't need to check more combos of b,c
        while a**2 + b**2 <= c**2:

            # if current values form Pythagorean triple, increment total
            if a**2 + b**2 == c**2:
                totalTriplets += 1
            
            # incrementing b and decrementing c for next loop runthrough
            # a+b+c = n is still true since a is unchanged at this point,
            # and net changes to b+c is 0
            b += 1
            c -= 1

        # setup for next loop runthrough
        a += 1
        b = a
        c = perimeter - a - b

    return totalTriplets


def maxPythagoreanTriplets(limit):

    maxSolutions = 0
    maxPerimeter = 0
    
    # strictly max answer will never be in lower half of perimeter
    for perimeter in range (int(limit/2), limit):
        solutions = pythagoreanTripletsByPerimeter(perimeter)
        if solutions > maxSolutions:
            maxSolutions = solutions
            maxPerimeter = perimeter

    return maxPerimeter, maxSolutions


# optimised solution
def optimisedMaxPythagoreanTriplets(limit):

    # array to store results
    perimeterTriplets = [0] * limit

    a = 1

    # where a = b = 1, c = sqrt(2)
    # this is largest possible ratio of a+b : c
    # once we exceed this ratio we can break out of loop
    while a <= limit / (2 + sqrt(2)):
        
        # initialising b here since we only need to generate triplets with
        # perimeter in upper half of limit
        # initialising to a instead if that is larger, as b >= a always
        b = max(int(limit/4) - a, a)
        
        while a + b <= 2*limit / (2 + sqrt(2)):

            # using Pythagorean to work out c 
            c = sqrt(a**2 + b**2)

            # check to see if c is an integer and perimiter was within given limit
            if c%1 == 0 and a+b+c < limit:
                perimeter = int(a+b+c)
                perimeterTriplets[perimeter] += 1
            b += 1
        a += 1


    # finding largest element of array to return results
    maxPerimeter = 0
    maxTriplets = 0

    # only need to check 2nd half
    for i in range(int(limit/2), limit):
        if perimeterTriplets[i] > maxTriplets:
            maxPerimeter = i
            maxTriplets = perimeterTriplets[i]

    return maxPerimeter, maxTriplets



# runs both implementations of solution and prints how long it takes to complete each one
def timeCompare(limit):
    start = time()
    perimeter, solutions = optimisedMaxPythagoreanTriplets(limit)
    end = time()
    
    print (f'There are {solutions} right angle triangles with integral length sides and a perimeter of {perimeter}')
    print (f'This is the most solutions for any perimeter below {limit}')
    print ('Time taken to compute:')
    print (f'optimisedMaxPythagoreanTriplets({limit}) - {end - start} seconds')

    start = time()
    perimeter, solutions = maxPythagoreanTriplets(limit)
    end = time()
    
    print (f'maxPythagoreanTriplets({limit}) - {end - start} seconds')


timeCompare(1000)
timeCompare(10000)
