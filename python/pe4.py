def reverse(n):
    revn = 0
    while n > 0:
        revn = revn*10 + n%10
        n = int (n / 10)
    return revn

def palindromic(n):
    return n == reverse(n)

def largestPalindromicProduct(digits, printcalc=""):
    x = 10**digits - 1
    y = 10**digits - 1
    pal = 0
    palx = 0
    paly = 0
    while y > 0 and y*(10**digits-1) > pal:
        while x > 0 and x*y > pal:
            if palindromic(x*y) and x*y > pal:
                pal = x*y
                palx = x
                paly = y
            x = x - 1
        y = y - 1
        x = 10**digits - 1
    if printcalc == "y":
        print (palx, "*", paly, "=", pal)
    return pal

largestPalindromicProduct(3, printcalc="y")



