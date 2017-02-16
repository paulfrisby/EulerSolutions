from time import *

def collatzCount(lim):
    iterations = [0]
    longestchain = 0
    startnum = 0
    for i in range (1, lim):
        chain = 1
        j = i
        while j != 1:
            if j % 2:
                j = 3*j + 1
            else:
                j = j / 2
            if j < i:
                chain += iterations[j]
                j = 1 
            else:
                chain += 1
        iterations += [chain]
        if chain > longestchain:
            startnum = i
            longestchain = chain
    return [startnum, longestchain]

start = clock()
print collatzCount(1000000)[0]
end = clock()
print "time taken:", (end - start), "seconds"      
