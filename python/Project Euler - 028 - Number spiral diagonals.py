#pe28

def spiralDiagSum(n):
    total = 1
    for i in range( (n-1) / 2):
        total += 4 * ( ((2*i)+1)**2 ) + 10 * (2*(i+1))
    return total

print spiralDiagSum(1001)
