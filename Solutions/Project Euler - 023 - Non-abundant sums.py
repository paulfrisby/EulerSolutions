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
# Pseudocode
# ------------------------------------------------------------------------------
"""
general outline / plan of approach to problem
explanation of insights in to problem may also be included here as necessary
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Extra Information
# ------------------------------------------------------------------------------
"""
optional section depending on problem
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

#returns list of proper divisors
def divisors(n):
    if n < 2:
        return []
    div = [1]
    divisor = 2
    while divisor**2 - 1 < n:
        if n % divisor == 0:
            div += [divisor]
            if n / divisor != divisor:
                div += [n/divisor]
        divisor += 1
    return div

# returns true if number is abundant
def abundant(n):
    return sum(divisors(n)) > n

# returns list of abundant numbers up to a given limit
def abundantList(lim):
    alist = []
    for n in range(lim):
        if abundant(n):
            alist += [n]
    return alist

check = []
for i in range(28124):
    check.append(i)
    
abun = abundantList(28124)
x = len(abun)
for i in range(x):
    for j in range(i - 1, x):
        if abun[i] + abun[j] < 28124:
            check[abun[i] + abun[j]] = 0
print (sum(check))
