# ------------------------------------------------------------------------------
# Project Euler - Problem 042 - Coded triangle numbers
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=042
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using p042_words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
Open p042_words.txt
Add each word in file to wordlist
Close p042_words.txt

generate list of  100 triangular numbers
# should give comfortable headroom, covers words up to almost 200 letters long

counter = 0
for each word in wordlist:
    lettercount = 0
    for each char in word:
        lettercount = lettercount + alphabetalposition(char)
    if lettercount is in triangular number list:
        increment counter

print counter
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# File structure
# ------------------------------------------------------------------------------
"""
The p042_words.txt file contains a number of words all in a single line.

Each word is surrounded by double quotation marks, and there is a comma in
between each entry.

Each letter in the word is upper case.

Below is a preview of the start of the file:

"A","ABILITY","ABLE",

We can use the quotation marks to see when we have finished reading a word.

We can use the commas to split each word
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

import os

# move directory so file from different folder can be imported
os.chdir("..\ProblemData")

wordsFile = open('p042_words.txt')
words = wordsFile.read()
wordsFile.close()
words = words.replace('"', '').split(',')

triangularNumbers = []
for i in range(1,100):
    triangularNumbers.append(int((i/2)*(i+1)))

triangleWords = 0
for word in words:

    # work out total of letters' alphabet positions 
    letterTotal = 0
    for letter in word:
        # since ord('A') = 65, ord('B') = 66 et cetera
        letterTotal += ord(letter) - 64

    # increment counter if this word is triangular
    if letterTotal in triangularNumbers:
        
        # prints triangular word without a newline after
        print (word, end=' ')
        triangleWords += 1

print (f'\nThere are a total of {triangleWords} triangular words in "p042_words.txt"')                        
