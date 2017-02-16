from math import *
from time import clock

def isPrime(n):
    if  n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for divisor in range(3, int(sqrt(n)) + 1, 2):
            if n%divisor == 0:
                return False
        return True

def nthPrimeTrialDiv(n):
    p = 0
    i = 0
    while i < n:
        p = p + 1
        if isPrime(p):
            i = i + 1
    return p

def primesSieve(limit):
    primes = range(limit)
    primes[1] = 0
    p = 2
    while p + 2 < limit:
        p += 2
        primes[p] = 0
    p = 3
    while p*p < limit:
        mult = p*p
        diff = 2*p
        while mult < limit:
            primes[mult] = 0
            mult += diff
        p += 2
        while primes[p] == 0:
            p += 2            
    return primes

def nthPrime(n):
    if n < 6:
        return nthPrimeTrialDiv(n)
    primes = primesSieve( int( n * log(n) + n * log(log(n)) ) ) # upper bound of approximation for value of nth prime 
    pcount = 0
    for i in range(len(primes)):
        if primes[i] != 0:
            pcount += 1
        if pcount == n:
            return primes[i]


start = clock()
print nthPrimeTrialDiv(10001)
end = clock()
print "Trial Division method - time taken:", (end - start), "seconds"


start = clock()
print nthPrime(10001)
end = clock()
print "Sieve of Eratosthenes method - time taken:", (end - start), "seconds"
