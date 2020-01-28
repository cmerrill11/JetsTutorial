import random
import numpy as np
import matplotlib.pyplot as plt
import sys 

# Create the CDF
samples = int(sys.argv[3])
domain_min = int(sys.argv[1])
domain_max = int(sys.argv[2])

x_pos = np.linspace(domain_min,domain_max,samples)

y_array = np.exp(-x_pos)

pdf = y_array/float(y_array.sum()) # Why divide by the sum? 

cdf = pdf.cumsum()

# generate random number, set it equal to some probability, find the corresponding x

x_sample = np.zeros(samples)

for r,val in enumerate(x_sample):
    argminimum = np.argmin(abs(cdf-random.random()))
    x_sample[r] = x_pos[argminimum]

fig, ax = plt.subplots(1,3)
fig.set_size_inches(11,4)

ax[0].plot(x_pos,y_array)
ax[1].plot(x_pos,cdf)
ax[2].hist(x_sample, bins = 100)
mean = x_sample.mean()
std_dev = x_sample.std()
ax[2].set_xlabel("Mean = {0:0.2f} Std. Dev = {1:0.2f}".format(mean,std_dev))


fig.savefig('../Data/inversetransform.png')


