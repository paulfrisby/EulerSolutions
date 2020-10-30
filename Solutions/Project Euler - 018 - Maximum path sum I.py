# ------------------------------------------------------------------------------
# Project Euler - Problem 018 - Maximum path sum I
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=018
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

Find the maximum total from top to bottom of the triangle below:

                             75
                           95  64
                         17  47  82
                       18  35  87  10
                     20  04  82  47  65
                   19  01  23  75  03  34
                 88  02  77  73  07  63  67
               99  65  04  28  06  16  70  92
             41  41  26  56  83  40  80  70  33
           41  48  72  33  47  32  37  16  94  29
         53  71  44  65  25  43  91  52  97  51  14
       70  11  33  28  77  73  17  78  39  68  17  57
     91  71  52  38  17  14  91  43  58  50  27  29  48
   63  66  04  68  89  53  67  30  73  16  69  87  40  31
 04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method! ;o)
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
# Triangle
# ------------------------------------------------------------------------------
triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------


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


print (maxPathSum(triangle))
