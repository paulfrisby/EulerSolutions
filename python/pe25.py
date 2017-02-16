def digits(n):
    tot = 0
    while n > 0:
        n = n / 10
        tot += 1
    return tot

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

print fibDigits(1000)
