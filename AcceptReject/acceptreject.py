import numpy as np
import matplotlib.pyplot as plt
import random
import sys

# evaluate a PDF for a value of x
def normal_y(val_x):
    normal_y = np.exp(-val_x) #pdf goes 
    return normal_y

# returns a random value of x that obeys given pdf 
def rand_x(x_max,y_coef):
    
    value = 0
    time = 0 
    
    while value == 0:
        rand_x = random.random()*x_max
        rand_y = random.random()*y_coef
    
        pdf_y = normal_y(rand_x)
        
        time = time + 1
        
        if rand_y < pdf_y:
           value = rand_x
            
           return value, time
        
        else: 
            continue

x_max = int(sys.argv[1])
y_coef = float(sys.argv[2])

#Actually generating random numbers

normal_x = np.zeros([1000])
tries = np.zeros([1000])

for idx,value in enumerate(normal_x):
    rand_x_return = rand_x(x_max,y_coef)
    normal_x[idx] = rand_x_return[0]
    tries[idx] = rand_x_return[1]

fig, ax = plt.subplots(1,2)

ax[1].hist(normal_x,bins = 100)

# Normalize the distribution
# Gotta divide individual areas by the cumulative histogram area

heights = np.zeros(100) # This should be the number of bins in the hi
bins = np.linspace(0,5,101) 

# This aint the sexiest way to do it but it's working!
for idx in range(100):
    values = np.where((bins[idx] < normal_x) & (normal_x < bins[idx+1]))
    heights[idx] = len(normal_x[values])

areas = heights*bins[1]
normalized = areas/areas.sum()
ax[1].bar(bins, heights, width = 5/101, align = 'edge')

# create a plot of the PDF we are matching

plt_x = np.linspace(0,10,1000)
plt_y = np.zeros(1000)

for idx,val in enumerate(plt_x):
    plt_y[idx] = normal_y(plt_x[idx])

ax[0].plot(plt_x,plt_y)

eff = 1000/tries.sum()
ax[1].set_xlabel("the efficiency was {0:f}".format(eff))
fig.savefig('../Data/acceptreject.png')
