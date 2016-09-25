"""

Monte Carlo Simulation for estimation of value of PI
The circle has radius 1 unit and it's centre is at origin
The square is therefore circumscribed on the circle with its appropriate sides parallel to the axis

"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Initialization of Variables

count = 0               # Used to make 500 experiments
piTrials = [None] * 0   # Used to store value of the 500 estimates values of PI
error = [None] * 0      # Used to store error of the 500 estimates values of PI
piMean = 0.0            # Used to store the mean value of the 500 estimates of PI
noOfTrials = 500.0

# Calculating 500 estimates of PI

while count < noOfTrials:
    m1 = 2000.0
    m = 2000
    limit = 1.0
    sampleX = np.random.uniform(-limit, limit, m)  # Stores the randomly generated x co-ordinate of the points
    sampleY = np.random.uniform(-limit, limit, m)  # Stores the randomly generated y co-ordinate of the points
    n = 0.0

    for i, j in zip(sampleX, sampleY):             # Finds out which points lie in the circle
        dist = i**2 + j**2
        if dist < 1:
            n += 1

    piTrials.append(n / m1 * 4.0)
    piMean += n / m1 * 4.0
    count += 1

#
piMean /= noOfTrials  # Calculates the mean of the estimated values
print piMean
stdDeviation = np.std(piTrials)   # Calculating the standard deviation of the estimates of PI
print stdDeviation
error[:] = [x - math.pi for x in piTrials]  # error of the estimated value from the actual value of PI
print error
plt.hist(piTrials, 23, normed=1, facecolor='green')  # Plotting the histogram
plt.show()
