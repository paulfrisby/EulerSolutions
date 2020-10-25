# returns number of letters in english spelling of any number from 0 to 9999
def numLetterCount(n):
    letters = 0
    lcount = [[0, 3, 3, 5, 4, 4, 3, 5, 5, 4], [0, 3, 6, 6, 5, 5, 5, 7, 6, 6], [0, 10, 10, 12, 11, 11, 10, 12, 12, 11], [0, 11, 11, 13, 12, 12, 11, 13, 13, 12]]
    teens = [3, 6, 6, 8, 7, 7, 7, 9, 9, 8]
    digits = 0
    if n > 100 and n % 100 != 0:
        letters = 3
    while digits < 4:
        if digits == 0 and (n / 10) % 10 == 1:
            letters += teens[n % 10]
            n = n / 100
            digits += 2
        else:
            letters += lcount[digits][n % 10]
            n = n / 10
            digits += 1
    return letters


total = 0
for x in range(1001):
    total += numLetterCount(x)
print total
