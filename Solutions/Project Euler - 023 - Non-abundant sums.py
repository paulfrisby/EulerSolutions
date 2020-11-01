# ------------------------------------------------------------------------------
# Project Euler - Problem 023 - Non-abundant sums
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=023
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

#returns list of proper divisors
def divisors(n):

    # 1 has no proper divisor
    if n < 2:
        return []

    # 1 is a proper divisor of every number larger than 1
    divisors = [1]
    
    divisor = 2
    while divisor**2 <= n:
        if n % divisor == 0:
            divisors.append(divisor)

            # if divisor is not square root of n, adds invers divisor too
            if n/divisor != divisor:
                divisors.append(n/divisor)
                
        divisor += 1
    return divisors


# returns true if number is abundant
def abundant(n):
    return sum(divisors(n)) > n


# returns list of abundant numbers up to a given limit
def abundantList(lim):
    abundantList = []
    for n in range(lim):
        if abundant(n):
            abundantList.append(n)
    return abundantList


# create a list of numbers up to 28,124
check = []
for i in range(28124):
    check.append(i)
    
# creat list of abundant numbers under 28124
abun = abundantList(28124)

aLen = len(abun)

# iterate through each possible combination of 2 abundant numbers
for i in range(aLen):
    for j in range(i, aLen):
        if abun[i] + abun[j] < 28124:

            # update checklist to 0 to show that number can be written in required form
            check[abun[i] + abun[j]] = 0

# sum remaining numbers to get total of all numbers that can't be written as sum of 2 abundant numbers
print (f'The sum of all the positive integers which cannot be written as the sum of two abundant numbers is {sum(check)}')
