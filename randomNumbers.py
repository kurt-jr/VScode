import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import chi2
np.random.seed(12345)
data = [np.random.standard_normal() for i in range(7)]
print(data)
plt.hist(data)

#normal distribution
x = np.random.randn(1000)
plt.hist(x, bins=30, color='skyblue', edgecolor='black')

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')

#uniform distribution 
y = np.random.uniform(999)
plt.hist(y, color = 'red', edgecolor = 'black')


#chi squared distribution
#chi2 = stats.chi2(5)
chi2 = np.random.chisquare(10, 10000)

# Plot the histogram
plt.hist(chi2, bins=20)