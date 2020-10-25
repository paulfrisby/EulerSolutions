#pe24

def factorial(n):
    f = n
    for i in range(1, n):
        f = f * i
    return f

# returns the nth permutation (ordered lexicographically) of elements in list, objects
def perm(objects, n):
    objects.sort()
    p = ''
    n -= 1
    x = len(objects)
    while x > 1:
        tot = factorial(x) / x 
        p += str(objects[n / tot])
        del objects[n / tot]
        n = n % tot
        x -= 1
    p += str(objects[0])
    return p

print perm([0, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1000000)
