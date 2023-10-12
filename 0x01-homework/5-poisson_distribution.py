import numpy as np
from scipy.stats import poisson

average_rate = 3.0
x_values =np.arange(0, 11) #the number of events from 1 up to 10

pmf_values = poisson.pmf(x_values, average_rate)

print(pmf_values)

