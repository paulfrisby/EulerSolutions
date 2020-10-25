from math import *
from time import *

# returns ordered list of factors of n
def orderedFactors(n):
    if n < 1:
        return []
    if n == 1:
        return [1]
    factors = [1]
    for i in range(2, n/2 + 1):
        if n % i == 0:
            factors += [i]
    factors += [n]
    return factors

# returns unordered list of factors of n
def factorList(n):
    if n < 1:
        return []
    if n == 1:
        return [1]
    factors = [1, n]
    for i in range(2, int( sqrt(n) ) + 1):
        if n % i == 0:
            factors += [i, n/i]
    return factors

# returns nth triangle number
def triangular(n):
    return int(0.5 * n**2 + 0.5 * n)

# returns first triangular number with more than n factors
def triFactors(n):
    i = 1
    t = 1
    while True:
        if len( factorList(t) ) > n:
            return t
        i += 1
        t += i


start = clock()
print triFactors(500)
end = clock()
print "time taken:", (end - start), "seconds"
