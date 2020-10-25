def sumOfPowers(power, upto):
    x = 1
    sumx = 0
    while x - 1 < upto:
        sumx = sumx + x**power
        x = x + 1
    return sumx

def powerOfSums(power, upto):
    x = 1
    sumx = 0
    while x - 1 < upto:
        sumx = sumx + x
        x = x + 1
    return sumx**power

def diffOfPowers(power, upto):
    return powerOfSums(power, upto) - sumOfPowers(power, upto)

print diffOfPowers(2, 100)

