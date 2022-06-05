"""
1. Given the definition of the geometric Point class, complete the function named distance:
def distance(r1, r2):
# Details go here
that returns the distance between the two points passed as parameters.
"""
import math


def distance(r1, r2):
    d = math.sqrt((r2[0] - r1[0]) ** 2 + (r2[1] - r1[1]) ** 2)
    return d


# (x , y) for example :
print(distance((1, 2), (4, 2)))
