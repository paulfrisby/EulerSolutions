# pe31

cValues = [200, 100, 50, 20, 10, 5, 2, 1] # values in pence of available coins

def initialCombo(p):
    combo = []
    for coin in cValues:
        for i in range(p / coin):
            combo = [coin] + combo
        p = p % coin
    return combo

def cBreak(p):
    v = p
    combo = []
    for coin in cValues:
        if coin != v:
            for i in range(p / coin):
                combo = [coin] + combo
            p = p % coin
    return combo

# given monetary value in pence, returns number of ways this can be reached using british coins
def coinCombos(p):
    combo = initialCombo(p)
    count = 1
    while len(combo) < p:
        for i, coin in enumerate(combo):
            if coin != 1:
                combo = combo[:i] + cBreak(coin) + combo[i + 1:]
                break
        count += 1
    return count


for i in [1, 2, 5, 10, 200]:
    print i, "has", coinCombos(i), "combinations"

# currently returns too small a value, e.g. 5 x 2p = 10p combo isn't counted
