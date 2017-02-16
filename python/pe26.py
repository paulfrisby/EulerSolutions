def digits(n):
    if n / 10 == 0:
        return 1
    else:
        return 1 + digits(n / 10)


# if 1/n has a repeating decimal this returns the length in digits of the recurring cycle, otherwise returns 0
def decExpansion(n):
    div = 10 ** digits(n - 1)
    if div % n == 0:
        return [[div/n, 0]]
    dec = []
    for j in range(digits(n - 1) - 1):
        dec += [[0, 0]]
    dec += [[div / n, div % n]]
    while True:
        dec += [[dec[-1][1] * 10 / n, dec[-1][1] * 10 % n]]
        if dec[-1][1] == 0 and len(dec) > 1:
            return dec
        for i in range(len(dec) - 1):
            if dec[i][0] == dec[-1][0] and dec[i][1] == dec[-1][1]:
                return dec


def repeatDigits(n):
    dec = decExpansion(n)
    for i in range(len(dec) - 1):
         if dec[i][0] == dec[-1][0] and dec[i][1] == dec[-1][1]:
             return len(dec) - 1 - i


def decStr(n):
    decstr = '0.'
    dec = decExpansion(n)
    for i in range(len(dec) - 1):
        if dec[i][0] == dec[-1][0] and dec[i][1] == dec[-1][1]:
            decstr += '('
        decstr += str(dec[i][0])
    decstr += ')'
    return decstr


h=0
for i in range (1,1000,2):
    j = repeatDigits(i)
    if j>h:
        h=j
        bob=i
print '1 /', bob, '=', decStr(bob)


    
    
    




