from time import clock

def pythagoreanTriplet(n):
    i = n / 2
    while i > 0:
        j = 1
        k = n - i - 1
        while j < k + 1:
            if i**2 + j**2 == k**2:
                return [i, j, k, i*j*k]
            j += 1
            k -= 1
        i -= 1

tripsum = 1000
print "Where a^2 + b^2 = c^2 & a + b + c =", tripsum
print "a, b, c & a*b*c are:"
start = clock()
print pythagoreanTriplet(tripsum)
end = clock()
print "time taken:", (end - start), "seconds"
        
        
    


    

            
    

