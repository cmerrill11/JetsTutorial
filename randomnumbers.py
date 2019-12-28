import matplotlib.pyplot as plt
import numpy as np
import random

# Creat an array to put all the random numbers inside
numbers = np.zeros(1000)

# Fill the array with random numbers
for idx,val in enumerate(numbers):
    val = random.random()
    numbers[idx] = val

# Adjust the bounds so that the numbers fall between 5 and 15 
new_numbers = (numbers*10)+5

# Plot a histogram of the numbers
fig, ax = plt.subplots(1,1)
ax.hist(new_numbers, bins=100)

# Plot the mean
mean = new_numbers.mean()
ax.hlines(mean,5,15)
ax.text(12,15,"The mean is {0:0.2f}".format(mean))

fig.savefig('./Data/fig1.png', bbox_inches = 'tight')

