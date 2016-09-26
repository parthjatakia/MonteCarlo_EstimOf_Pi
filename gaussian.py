"""

Gaussian distriibution with parameter mu and sigma

"""
import  pylab as pl
import numpy as np

e=2.718281828
pi=3.141592654

# Plot three gaussian distributions with (mu,sigma) = (0,10),(10,10) and (0,20) to observe dependence on parameters
mu = (0,10,0)
sigma = (10,10,20)
for i in range(3):
    x = np.linspace(mu[i]-70,mu[i]+70,200)  # 200 evenly spaced points between mu-70 and mu+70
    y = pl.normpdf(x,mu[i],sigma[i])        # Calculate values of gaussian pdf with parameters mu[i] and sigma[i]
    pl.plot(x,y)                            # Plot calculated values

pl.show()