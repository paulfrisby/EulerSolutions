# ------------------------------------------------------------------------------
# Project Euler - Problem 022 - Names scores
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=022
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
Using p022_names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns position in alphabet of upper case letter
def letterVal(char):
    return ord(char) - 64


# returns sum of alphabet positions of characters in name
def nameVal(name):
    val = 0
    for letter in name:
        val += letterVal(letter)
    return val


# open file and process names in to a list of strings
namesFile = open('p022_names.txt')
names = namesFile.read()
namesFile.close()
names = names.replace('"', '').split(',')

# sort list in to alphabetical order
names.sort()

total = 0
for i in range(len(names)):
    total += (i + 1) * nameVal(names[i])
print (f'The total of all the name scores in "p022_names.txt" is {total}')
