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

def digits(n):
    return len(str(n))

# returns n, where nth term of fibonacci sequence being first to have d digits 
def fibDigits(d):
    f1 = 1
    f2 = 1
    n = 1
    while True:
        if digits(f1) == d:
            return n
        if digits(f2) == d:
            return n + 1
        f1 = f1 + f2
        f2 = f1 + f2
        n += 2

print (fibDigits(1000))
