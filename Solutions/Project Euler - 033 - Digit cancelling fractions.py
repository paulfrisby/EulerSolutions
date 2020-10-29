# ------------------------------------------------------------------------------
# Project Euler - Problem 033 - Digit cancelling fractions
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=033
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
isFalseSimplificationEqual(numerator, denominator)
    return 1 if equal
    return 0 if not equal
    return -1 if not able to be simplified in this specific false way

    set up empty array of answers

for every numerator from 11 to 99:
    for every denominator from (numerator+1) to 99:
        if isFalseSimplificationEqual(numerator, denominator) returns 1:
            add numerator / denominator to array of answers

multiply together all the fractions in answer array
simplify result
get denominator, this is the final result
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# function which checks whether a positive fraction can be crudely simplified (returns -1 if not or for trivial examples)
# if it can it checks if crude simplification is equal to actual simplification
# returns 1 if equal and 0 if not
def isCrudeSimpEqual(numerator, denominator):

    # the crude method only applies to 2 digit numerator/denominators, this checks that
    if not(numerator>9 and numerator<100) or not(denominator>9 and denominator<100):
        return -1

    # multiples of 10 are defined as trivial examples and are thus excluded
    elif (numerator%10 == 0) or (denominator%10 == 0):
        return -1

    # checks if no digit is shared between numerator and denominator
    elif not(numerator%10==int(denominator/10) or int(numerator/10)==denominator%10 or numerator%10==denominator%10 or int(numerator/10)==int(denominator/10)):
        return -1

    # checks to see which digit is shared and if the crude simplification in that case is correct
    else:
        # num unit digit == denom tens digit
        if numerator%10==int(denominator/10) and numerator/denominator == (int(numerator/10)) / (denominator%10):
            return 1
        # num tens digit == denom unit digit
        if int(numerator/10)==denominator%10 and numerator / denominator == (numerator%10) / (int(denominator/10)): 
            return 1  
        # share unit digit       
        if numerator%10==denominator%10 and numerator/denominator == (int(numerator/10)) / (int(denominator/10)):
            return 1    
        # share tens digit
        if int(numerator/10)==int(denominator/10) and numerator/denominator == (numerator%10) / (denominator%10):
            return 1
        # crude simplification does not work with any combination of digits   
        return 0
            

# initialising empty arrays to store numerator/denominator of fractions which simplify correctly using crude method
numerators = []
denominators = []

# iterating from 11 to 99 in numerator and from numerator+1 to 99 in denominator, as we only want to check fractions less than 1
for i in range(11,100):
    for j in range(i+1,100):
        if isCrudeSimpEqual(i,j) == 1:
            numerators.append(i)
            denominators.append(j)


# initialising numerator/denominator to 1 so that we can multiply it subsequent fractions as 1 is the multiplicative identity          
numeratorProduct = 1
denominatorProduct = 1

# iterating through arrays of numerators and denominators of fractions which correctly simplify using the crude method
for i in range(len(numerators)):
    # prints the original fraction as well as the crude simplification
    print(numerators[i], "/", denominators[i], "=", int(numerators[i]/10), "/", (denominators[i]%10))
    # works out a running product of numerator and denominator of crude simplification
    numeratorProduct = numeratorProduct * int(numerators[i]/10)
    denominatorProduct = denominatorProduct * (denominators[i]%10)


# simplifies if fraction can be cancelled down to 1/n
if denominatorProduct % numeratorProduct == 0:
   denominatorProduct = int (denominatorProduct /  numeratorProduct)
   numeratorProduct = 1

    
# prints product of crudely simplified fractions
print ("product of above fractions = ", numeratorProduct, "/", denominatorProduct)
