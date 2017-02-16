def largestPrimeFactor(num):
    x = num
    p = 2
    if x%2 == 0:
        while x > p:
            if x % p == 0:
                x = x / p
            else:
                p = p + 1
    else:
        p = p + 1
        while x > p:
            if x % p == 0:
                x = x / p
            else:
                p = p + 2
    return p

print largestPrimeFactor(600851475143)
