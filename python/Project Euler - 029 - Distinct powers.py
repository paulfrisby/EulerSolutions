# pe29

def powerSet(a, b): 
    powers = []
    for i in range(2, a):
        for j in range(2, b):
            powers += [i**j]
    return set(powers)

print len(powerSet(101, 101))
