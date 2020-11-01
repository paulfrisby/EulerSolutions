# ------------------------------------------------------------------------------
# Project Euler - Problem 067 - Maximum path sum II
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=067
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""


By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in p067_triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Pseudocode
# ------------------------------------------------------------------------------
"""
Working from bottom up, we can work out the maximum sum from current position
to end by adding the larger of the 2 values below our current position to the
value in current position.

Once we have done this all the way to the top, the top most element will be
equal to the maximum path.

Example:

    3                3                   3                   3               
   7 4             7   4               7  4    -->      7+13  4+15    -->        
  2 4 6   -->   2+8 4+9 6+9   -->    10 13 15         10    13    15              
 8 5 9 3       8   5   9   3        8  5  9  3       8   5      9   3            


          3        -->     3+20       -->      23       -->  Max path = 23       
 -->   20  19            20    19            20  19
     10  13  15        10   13   15        10  13  15 
    8  5    9  3      8  5    9    3      8  5    9  3 
 
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

import os


# returns maximum sum from top to bottom of trianglar matrix
def maxPathSum(matrix):
    rows = len(matrix)

    # working backwards from penultimate row to 0th row
    for i in range(rows-1)[::-1]:
            
        # for each number in row add the larger  adjacent value from below
        for j in range(len(matrix[i])):
            if matrix[i+1][j] > matrix[i + 1][j + 1]:
                matrix[i][j] += matrix [i+1][j]
            else:
                matrix[i][j] += matrix [i+1][j + 1]
    return matrix[0][0]


# move directory so file from different folder can be imported
os.chdir("..\ProblemData")

# building triangle matrix from text file
triangleFile = open('p067_triangle.txt')
triangle = []

# since we know there are 100 lines
for i in range(1, 101):
    row = []

    # since we know each line has i numbers
    for j in range(i):

        # since each number is followed by a space or newline
        # we read 3 bytes, then cast first 2 bytes to an int
        number = int(triangleFile.read(3)[:2])
        row.append(number)

    triangle.append(row)

triangleFile.close()
print (f'The maximum total from top to bottom of triangle in "p067_triangle.txt" is {maxPathSum(triangle)}')
