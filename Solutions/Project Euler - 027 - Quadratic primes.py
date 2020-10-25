from math import *

#pe27

# exhaustive check approach

# try every possible value of a & b
# for each see what number of consecutive primes it produces
# if it is greater than largest so far update variable
# return value

# use prime check function
# potentially use sieve of Eratosthenes and check against this instead

# 3,996,001 checks will need to be performed (1999 x 1999)
# improvements could be made with check that eliminates a,b combos earlier

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

def consecPrimes(a, b, count = 0):
    if isPrime(count*count + a*count + b):
        return consecPrimes(a, b, count + 1)
    return count
    

largest = 0
abprod = 0

for i in range (1000):
    for j in range(1000):
        if consecPrimes(i, j) > largest:
            largest = consecPrimes(i, j)
            abprod = i*j
            a = i
            b = j
        if consecPrimes(i*-1, j) > largest:
            largest = consecPrimes(i*-1, j)
            abprod = i*j*-1
            a = -i
            b = j
        if consecPrimes(i, j*-1) > largest:
            largest = consecPrimes(i, j*-1)
            abprod = i*j*-1
            a = i
            b = -j
        if consecPrimes(i*-1, j*-1) > largest:
            largest = consecPrimes(i*-1, j*-1)
            abprod = i*j
            a = -i
            b = -j
print "n*n + %dn + %d generates %d consecutive primes starting from n = 0, a * b = %d" % (a, b, largest, abprod)
        

