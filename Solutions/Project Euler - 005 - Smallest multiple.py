# ------------------------------------------------------------------------------
# Project Euler - Problem 005 - Smallest multiple
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=005
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
general outline / plan of approach to problem
explanation of insights in to problem may also be included here as necessary
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

def smallestMultiple(largestFactor):

    # setup for first loop runthrough
    smallestMultiple = 1
    previousMultiple = 1
    
    # iterates through every factor
    for i in range(1, largestFactor + 1):

        # runs until smallestMultiple is evenly divisible with current factor
        while not smallestMultiple%i==0:
            # adds smallestMultiple from previously calculated factors so new number is still divisible by all of them
            smallestMultiple += previousMultiple

        # setup for next loop runthrough
        previousMultiple = smallestMultiple
    
    return smallestMultiple

print (smallestMultiple(20))
