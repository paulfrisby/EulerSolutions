# ------------------------------------------------------------------------------
# Project Euler - Problem 043 - Sub-string divisibility
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=043
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the
following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
divisors = [-,-,-,2,3,5,7,11,13,17]
list = [1,2,3,4,5,6,7,8,9]

until numbers in list are 10 digits long:
    for each number in list:
        for each digit in '0123456789':
            concatenate to end of number (if digit isn't already there)
            if last 3 digits meet divisibility requirment:
                add to newlist
    set list = newlist (ready for next digit to be added)

print sum list
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------


# all posibilities for 1st digit
panList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# number that last 3 digits must evenly divide in to
divisors = [0,1,1,1,2,3,5,7,11,13,17]

# digit by digit generates all possible 0 to 9 pandigital numbers that fit all
# divisibility criteria up to that point
for i in range(2,11):
    newList = []
    for pan in panList:
        for digit in '0123456789':

            # only add unique digits
            if digit not in pan:
                newPan = pan + digit

                # checks if last 3 digits are evenly divided by required factor
                if i > 3:
                    if newPan[-3] == '0' and int(newPan[-2:])%divisors[i] == 0:
                        newList.append(newPan)
                    elif int(newPan[-3:])%divisors[i] == 0:
                        newList.append(newPan)

                # only runs for 2nd/3rd digit where no divisibility criteria
                else:
                    newList.append(newPan)

    # save list, ready for next digit to be added
    panList = newList

for i in range(len(panList)):
    panList[i] = int(panList[i])

print (f'The 0 to 9 pandigital numbers which share the sub-string divisibility property are:\n{panList}\nThe sum of these is {sum(panList)}')
