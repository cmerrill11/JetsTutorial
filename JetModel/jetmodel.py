import random 
import numpy as np
import matplotlib.pyplot as plt

"""
Model has to include two parts:
    1: the particles travel some distance
        This is completely determined by relativistic kinematics
    2: They split into two different particles:
        Splitting is:
            Soft: as in PDF(z) = 1/z where z is the fraction of the initial
                  particles energy
            Collinear: PDF(theta) = 1/theta for theta from 0 to 2pi. 
            
        These two random numbers give the characteristics of the
        the radiation. To allow the model to proceed, the kinematics of
        of the final state particle that emitted the radiation must 
        be determined. This can be done with one simplifiying assumption
        and by applying the law of conservation. 
        
        What is the simplifying assumption?
        I don't really know what this assumption is, however I am going to
        proceed anyway 
"""
# Create a random number generator that gives a zumeber from PDF(z) = 1/z

def z_fraction():
    x_pos = np.linspace(1e-3,1,1000)
    y_pos = 1/(x_pos)
    pdf = y_pos/(float(y_pos.sum()))
    cdf = pdf.cumsum()
    percent = random.random()
    argmin = np.argmin(abs(cdf-percent))
    x_sample = x_pos[argmin]
    return x_sample

# Do the same thing for the PDF(theta) = 1/theta
    
def random_theta():
    theta_pos = np.linspace(1e-3,np.pi/2,1000)
    y_pos = 1/(theta_pos)
    pdf = y_pos/(float(y_pos.sum()))
    cdf = pdf.cumsum()
    percent = random.random()
    argmin = np.argmin(abs(cdf-percent))
    theta_sample = theta_pos[argmin]
    return theta_sample
    
# Now makes the most sense to create an object that has a method for splitting. 
# but atm imma just code that up in an array and only use 2 dimensions. 

initial_parton = np.array(1,1,1)

time = random.random()

x_dist = initial_parton[] 