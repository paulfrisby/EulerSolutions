# ------------------------------------------------------------------------------
# Project Euler - Problem 019 - Counting Sundays
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=019
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
You are given the following information, but you may prefer to do some research
for yourself.

-1 Jan 1900 was a Monday.

- Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

- A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# days in each month
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sundayCount = 0

# let days go from Sunday to Saturday, 0 to 6
# it was a Tuesday on Jan 1st 1901
day = 2

# for each month in the range check the day on the 1st
for year in range(1901, 2001):
    for month in range(12):

        # if it is a Sunday, increment counter
        if day == 0:
            sundayCount += 1

        # set day for next month

        # leapyear
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            # adding modulo 7 will keep result in range of 0 to 6
            day = (day + leapMonths[month]) % 7

        # non-leapyear
        else: 
            day = (day + months[month]) % 7

print (sundayCount)
