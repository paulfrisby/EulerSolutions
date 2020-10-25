def smallestDiv(upto):
    x = 1
    prevx = 0
    i = 1
    while i < upto + 1:
        if x%i==0:
            prevx = x
            i = i + 1
        else:
            x = x + prevx
    return x

print smallestDiv(20)
