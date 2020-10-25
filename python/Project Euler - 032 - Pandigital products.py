def isPan(s):
    if len(s) != 9:
        return False
    for num in "123456789":
        if num not in s:
            return False           
    return True

products = []
for i in range(100, 5000):
    for j in range(2, 100):
        if 999 < i*j < 10000:
            products += [[i, j, i*j]]

print "The following identities containing multiplicand, multiplier, & product are 1 to 9 pandigital:"

pandigital = []
for p in products:
    if isPan(str(p[0]) + str(p[1]) + str(p[2])):
        print p[0], "*", p[1], "=", p[2]
        pandigital += [p[2]]

print "The sum of the unique products is", sum(set(pandigital))
