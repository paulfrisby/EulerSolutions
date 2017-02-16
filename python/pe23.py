#returns list of proper divisors
def divisors(n):
    if n < 2:
        return []
    div = [1]
    divisor = 2
    while divisor**2 - 1 < n:
        if n % divisor == 0:
            div += [divisor]
            if n / divisor != divisor:
                div += [n / divisor]
        divisor += 1
    return div

# returns true if number is abundant
def abundant(n):
    return sum(divisors(n)) > n

# returns list of abundant numbers up to a given limit
def abundantList(lim):
    alist = []
    for n in range(lim):
        if abundant(n):
            alist += [n]
    return alist

check = range(28124)
abun = abundantList(28124)
x = len(abun)
for i in range(x):
    for j in range(i - 1, x):
        if abun[i] + abun[j] < 28124:
            check[abun[i] + abun[j]] = 0
print sum(check)
        


        
    
