# implementation of an algorithm to solve project euler problem 1
# https://projecteuler.net/

# initialise a list to store all the multiples
multiples = []


# loop through every number below 1000
for number in range(1000):
    #check if it is a multiple
    if number%3==0 or number%5==0:
        # add it to the list only if it is
        multiples = multiples + [number]

# add together all the multiples worked out previously and print it
print sum(multiples)
