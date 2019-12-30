import numpy as np
import matplotlib.pyplot as plt
import random

"""
Generate random values that follow a gaussian distribution with:
mu = 5, sigma = 2, and the bounds at 0 and 10.
"""
# evaluate a PDF for a value of x
def normal_y(mu,sigma,val_x):
    normal_y = (1/(sigma*np.sqrt(2*np.pi)))*np.exp((-0.5)*((val_x-mu)/sigma)**2)
    return normal_y

# returns a random value of x obeys a gaussian 
def rand_x(x_max,y_coef):
    
    value = 0
    time = 0 
    
    while value == 0:
        rand_x = random.random()*x_max
        rand_y = random.random()*y_coef
    
        pdf_y = normal_y(mu,sigma,rand_x)
        
        time = time + 1
        
        if rand_y < pdf_y:
           value = rand_x
            
           return value, time
        
        else: 
            continue

# For the moment these are fixed but eventually I want to make these args from CL
sigma = 2
mu = 5

#Actually generating random numbers
normal_x = np.zeros([1000])
tries = np.zeros([1000])

for idx,value in enumerate(normal_x):
    rand_x_return = rand_x(10,0.25)
    normal_x[idx] = rand_x_return[0]
    tries[idx] = rand_x_return[1]

fig, ax = plt.subplots(1,1)

ax.hist(normal_x,bins = 100)

#create a plot of the guassian we are matching
plt_x = np.linspace(0,10,1000)
plt_y = np.zeros(1000)

for idx,val in enumerate(plt_x):
    plt_y[idx] = normal_y(mu,sigma,plt_x[idx])

ax.plot(plt_x,plt_y)

fig.savefig('./Data/hist.png')
"""
The graph isn't going to be normalized. To do that you have to divide each bin by
the total area covered by the bins.
"""
print(tries.sum())


