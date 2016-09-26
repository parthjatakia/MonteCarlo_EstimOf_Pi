"""

Binomial distribution with parameters n and p

"""
import  pylab as pl
import numpy as np
import scipy as sp

# Function to calculate aCb = a!/(b!)((a-b)!)
def choose(a,b):
    c = np.math.factorial(a) / (np.math.factorial(b) * np.math.factorial(a-b))
    return c

# Funcion to plot a Binomial distribution with parameters n and p
def plot_binomial(n,p):
    x = range(n+1)
    y=[0]*(n+1)
    for k in x:
        y[k] = choose(n,k) * p**k * (1-p)**(n-k)    # Calculate probability at each k from 0 to n

    pl.plot(x,y)                                    # Plot calculated probability distribution function

plot_binomial(30,0.3)
plot_binomial(50,0.3)
plot_binomial(30,0.7)
pl.show()