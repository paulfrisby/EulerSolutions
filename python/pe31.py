# https://projecteuler.net/problem=31
#
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#   1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


# PSEUDOCODE:
#coinCombinations(totalValue, coins)
#   if totalValue == 0 || totalValue == 1
#       return 1
#
#   else if totalValue < 0
#       return 0
#
#   else
#       return sum{
#           coinCombinations(totalValue-coins[0], coins)
#           coinCombinations(totalValue-coins[1], coins[1:])
#           ccoinCombinations(totalValue-coins[2], coins[2:])
#           ...
#           coinCombinations(totalValue-coins[n-1], coins[n-1:])
#           # only includes coins from this level or smaller, so that all combinations are calculated from largest to smallest
#           # should ensure no double counted combos
#       }
#
#print coinCombinations (200, allCoins)


allCoins = [200, 100, 50, 20, 10, 5, 2, 1] # values in pence of UK coins

def coinCombos(totalValue, coins):
    # base case, only 1 combination of coins makes 0
    if totalValue == 0:
        return 1

    # for when a larger coin than amount left over has been added to combi, making it invalid
    elif totalValue < 0:
        return 0

    else:
        totalCombos = 0
        
        for i in range(len(coins)):
            totalCombos += coinCombos(totalValue-coins[i], coins[i:])
            # coins slice only includes coins from this level or smaller, so all combos are calculated from largest to smallest
            # should ensure no double counted combos

        return totalCombos

print (coinCombos(200, allCoins))

