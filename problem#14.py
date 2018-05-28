# This problem was asked by Google.
# The area of a circle is defined as pi*r^2. Estimate pi to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

# pi*r^2 = Area of circle
# x^2 + y^2 = r^2
# 
# l * w = Area of square
# (2r) * (2r) = 4r^2 = Area of square
#
# Therefore, ratio(p) = Area of circle / Area of square
# p = pi*r^2 / 4r^2 = pi / 4
# pi = p * 4
#
# we can use monte carlo method to pick points on unit circle and get a ratio of the points that land inside the unit circle compared to the unit square.  Such a ratio is similar to area ratio of circle to square. == p

import random
import math

def findPi():
    random.seed()
    inCircle = 0.0
    inSquare = 0.0
    
    for i in range(0, 100000):
        x = random.random()
        y = random.random()

        if x**2.0 + y**2.0 <= 1.0:
            inCircle += 1.0
        inSquare += 1.0

    return (inCircle / inSquare) * 4.0
    

piMonteCarlo = findPi()
print "Estimate: %.3f" % piMonteCarlo
print "Actual: ", math.pi