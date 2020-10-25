# https://projecteuler.net/problem=34
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.


# returns n!
def factorial(n):
    
    # initialise variable to 1 to store result (as 1 is multiplicative identity)
    runningMult = 1

    # multiply by every integer up to and including n
    for i in range(1,n+1):
        runningMult = runningMult * i
        
    return runningMult


# returns the sum of the factorial of each digit of n, e.g. n = 234 returns 2! + 3! + 4!
def digitFactorialSum(n):

    # initialise variable to 0 to store result (as 0 additive identity)
    factorialSum = 0

    # deals with each digit in turn, starting from the last and working backwards
    while (n>0):
        lastDigit = n%10
        factorialSum += factorial(lastDigit)
        # truncates last digit, by dividing by 10 and rounding down (by casting to int)
        n = int(n/10)

    return factorialSum


# initialise variable to 0 to store result (as 0 additive identity)
runningSum = 0

# starting from 10, as single digit results are excluded as per definition
# stopping at 2 million as beyond this point the factorial sum will always be less than the number itself
# this is because n grows 10 times faster than the sum of the factorial of the digits of n 
for i in range(10,2000000):
    if i == digitFactorialSum(i):
        runningSum += i
        print(i) # printing out individual results, although not strictly required

print (runningSum)
