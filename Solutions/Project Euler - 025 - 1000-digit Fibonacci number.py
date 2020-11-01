# ------------------------------------------------------------------------------
# Project Euler - Problem 025 - 1000-digit Fibonacci number
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=025
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns n, where nth term of fibonacci sequence is first to have d digits 
def fibonacciDigits(d):
    fib1 = 1
    fib2 = 1
    term = 1
    while True:

        # checks to see if either of newly generated terms are long enough
        if len(str(fib1)) == d:
            return term
        if len(str(fib2)) == d:
            return term + 1

        # generate next 2 terms of sequence
        # fib1 = fib(n), f2 = fib(n+1)

        # fib(n) + fib(n+1) = fib(n+2)
        fib1 = fib1 + fib2

        # fib(n+1) + fib(n+2) = fib(n+3)
        fib2 = fib2 + fib1

        # since we are computing 2 new terms of sequence per loop
        term += 2


print (f'The index of the 1st term in the Fibonacci sequence to contain 1,000 digits is {fibonacciDigits(1000)}')
