# returns the number of possible routes from top left to bottom right for a x by y grid
def routeCount(x, y):
    routes = [[0] * x] * y
    routes += [[1] * x]
    for i in range(x):
        routes[i] += [1]
    j = x - 1
    while j >= 0:
        k = y - 1
        while k >= 0:
            routes[j][k] = routes[j + 1][k] + routes[j][k + 1]
            k -= 1
        j -= 1
    return routes[0][0]

print routeCount(20, 20)
    
