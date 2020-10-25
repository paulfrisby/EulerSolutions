# pe30

def isfifthSum(n):
    num = n
    fifthsum = 0
    while num > 0:
        fifthsum += (num % 10)**5
        num = num / 10
    return fifthsum == n


fifth = []
for i in range(2, 300000):
    if isfifthSum(i):
        fifth += [i]

print fifth, sum(fifth)
