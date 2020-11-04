# ------------------------------------------------------------------------------
# Project Euler - Problem 048 - Self powers
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=048
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10,405,071,317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# trivially easy to solve in python
# because of how it deals with numbers this large

selfPowerSum = 0
for integer in range(1,1001):
    selfPowerSum += integer**integer
    last10Digits = str(selfPowerSum)[-10:]
print (f'The last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000 are {last10Digits}')
    
