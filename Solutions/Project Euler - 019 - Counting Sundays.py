suncount = 0

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapmonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daycount = 2 # as it was a Tuesday on Jan 1st 1901
for year in range(1901, 2001):
    for month in range(12):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: # executes if it is a leapyear
            daycount = (daycount + leapmonths[month]) % 7
        else: 
            daycount = (daycount + months[month]) % 7
        if daycount == 0:
            suncount += 1

print suncount
