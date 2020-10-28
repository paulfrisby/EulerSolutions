# ------------------------------------------------------------------------------
# Project Euler - Problem 015 - Lattice paths
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=015
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Outline of approach
# ------------------------------------------------------------------------------
"""
- intialise a grid of vertices (for a nxn grid, are n+1xn+1 vertices), we are
aiming to work out the number of routes from each vertex to the goal

- for the bottom right vertex (where we are trying to reach) set a value of 1
as there is only 1 route to the goal if you are already there

- if you are in the bottom row or far right column, there is also only 1 route
to the goal (directly right or down respectively), so set every vertex of these
to 1 also

- for each vertex remaining, the number of routes is equal to the number of
routes of the vertex to the right plus the number of routes of the vertex below

- working backwards, from bottom to top, and from right to left, we can now
assign a value to every vertex in the grid

- after this is complete, the number of routes from topleft corner to bottom
right corner is equal to the value in the top left corner

- this should work for any size grid

Below is a visual example of the process for a 2x2 grid


       0--0--1       0--0--1       0--0--1       0--0--1       0--0--1     
3x3    |  |  |       |  |  |       |  |  |       |  |  |       |  |  |     
vertex>0--0--1  -->  0--w--1  -->  0--2--1  -->  x--2--1  -->  3--2--1  -->     
grid   |  |  |       |  |  |       |  |  |       |  |  |       |  |  |      
       1--1--1       1--1--1       1--1--1       1--1--1       1--1--1

                         w = 1 + 1 = 2               x = 2 + 1 = 3
   
       0--y--1       0--3--1       z--3--1      [6]-3--1      
       |  |  |       |  |  |       |  |  |       |  |  |      
  -->  3--2--1  -->  3--2--1  -->  3--2--1  -->  3--2--1  --> total routes = 6    
       |  |  |       |  |  |       |  |  |       |  |  |   
       1--1--1       1--1--1       1--1--1       1--1--1

           y = 1 + 2 = 3               z = 3 + 3 = 6
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns number of routes from top left to bottom right for an x by y grid
def routeCount(x, y):

    # initialising grid of vertices, bottom row / right column all equaling 1
    routes = [[0] * x] * y
    routes += [[1] * x]
    for i in range(x):
        routes[i] += [1]

    # working backwards along each row, from bottom to top
    row = x - 1 # 2nd last row
    while row >= 0:
        column = y - 1 # 2nd last column
        while column >= 0:
            # setting value of vertex to vertex below + vertex to right
            routes[row][column] = routes[row + 1][column] + routes[row][column + 1]
            column -= 1 # move left 
        row -= 1 # move up
    return routes[0][0]


print (f'There are {routeCount(20, 20)} possible routes from the top left to the bottom right of a 20x20 grid')
