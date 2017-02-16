from time import clock

# Paul Frisby - pafrisby@gmail.com

# sumOfPrimesSieve - function to sum all primes below a limit based on sieve of Eratosthenes.
#                    (list of numbers up to limit generated, all non-prime values sieved out, list summed)
#                    this is considerably quicker than using trial division
#0 - list of consecutive integers from 0 to limit-1 created - (0, 1, 2, 3, ..., limit-1)
#1 - 1(first positive non-prime value) set to 0.
#2 - p set to 2. (first prime)
#3 - starting from p^2, multiples of p up to limit found and set to 0. (in increments of 2p once p>2)
#    (starting from p^2 as lower non-prime values have been removed by previous p values)
#4 - finds next non-zero value in list if p+2 is non-prime, sets p to this as it is next prime.
#    repeats #3.
#5 - terminates once p^2 reaches limit, all non-zero numbers left in list are prime.
#    sums list for final result and returns it.
def sumOfPrimesSieve(limit):
    primes = range(limit) #0
    primes[1] = 0 #1
    p = 2 #2
    while p + 2 < limit: #3
        p += 2
        primes[p] = 0
    p = 3
    while p*p < limit: #3
        mult = p*p
        diff = 2*p
        while mult < limit:
            primes[mult] = 0
            mult += diff
        p += 2
        while primes[p] == 0: #4
            p += 2
            
    return sum(primes) #5


# checks whether a number is prime
def isPrime(n):
    if n == 2:
        return 1
    elif n < 2 or n%2 == 0:
        return 0
    else:
        divisor = 3
        check = 1
        while check == 1 and divisor*divisor < n + 1:
            if n%divisor == 0:
                check = 0
            divisor += 2
        return check

# uses trial division to sum all primes below a limit
def sumOfPrimes(to):
    if to < 3:
        return 0
    else:
        total = 2
        p = 3
        while p < to:
            if isPrime(p):
                total += p
            p += 2
        return total

print "sieve of Eratosthenes"
start = clock()
print sumOfPrimesSieve(2000000)
end = clock()
print "time taken:", (end - start), "seconds"

print "trial division"
start = clock()
print sumOfPrimes(2000000)
end = clock()
print "time taken:", (end - start), "seconds"
