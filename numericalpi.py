import numpy as np
import random
import sys
import matplotlib.pyplot as plt

# Function to generate pi approximations

def pi_values(n_total):

    accepted = 0

    for idx in range(n_total):
        
        x = random.random()
        y = random.random()

        dist = np.sqrt(x**2+y**2)
        
        if dist < 1:
            accepted = accepted + 1 
        else:
            continue
    
    pie = 4*(accepted/n_total)
    return pie

# Plot a histogram with several pi values

n_points = int(sys.argv[1])

n_for_histogram = int(sys.argv[2])

hist_array = np.zeros(n_for_histogram)

for idx,val in enumerate(hist_array):
    hist_array[idx] = pi_values(n_points)

fig, ax = plt.subplots(1,1)
ax.hist(hist_array, bins = 100)  

# Determine Mean and std. dev. of histogram

mean = hist_array.mean()
std_dev = hist_array.std()
ax.vlines(mean, 0, 40)
ax.set_xlabel("mean = {0:}, std. dev. = {1:f}".format(mean,std_dev))
fig.savefig('./Data/piehist.png')

