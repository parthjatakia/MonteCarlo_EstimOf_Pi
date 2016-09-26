 
import numpy as np
from scipy.stats import poisson
from matplotlib import pyplot as plt

# Define the distribution parameters to be plotted
mu = 20

# Initializing the array for the x values
x = np.arange(-1, 200)

# Plotting the graph. Some of the parameters are used for better display
plt.plot(x, poisson.pmf(x, mu), 'bo', ms=8, color='black', label=r'$\mu=%i$' % mu)

# Labelling and formatting the graphh
plt.xlim(-0.5, 30)
plt.ylim(0, 0.4)
plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu)$')
plt.title('Poisson Distribution')

# Showing the graph
plt.legend()
plt.show()
