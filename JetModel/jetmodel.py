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

def z():
    x_pos = np.linspace(1e-3,1,1000)
    y_pos = 1/(x_pos)
    pdf = y_pos/(float(y_pos.sum()))
    cdf = pdf.cumsum()
    percent = random.random()
    argmin = np.argmin(abs(cdf-percent))
    x_sample = x_pos[argmin]
    return x_sample

# Do the same thing for the PDF(theta) = 1/theta
    
def theta():
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
class particle(): 
    
    def __init__(self, gen, energy, px, py):
        self.gen = gen
        self.energy = energy
        self.px = px
        self.py = py
        
    def __str__(self):
        print(self.energy + " " + self.px + " " + self.pz)
        

def branch(p1, z, theta):
    if (p1.energy > 10**-2): 
    
        gen1 = p1.gen + 1
        energy1 = p1.energy * z
        px1 = p1.px * np.cos(theta)
        py1 = p1.py * np.sin(theta)    
        next1 = particle(gen1, energy1, px1, py1)
        
        energy2 = p1.energy - energy1
        px2 = p1.px - px1
        py2 = p1.py - py1
        next2 = particle(gen1, energy2, px2, py2)
        
        return branch(next1,z(),theta())+branch(next2,z(),theta())
    
    else:
        return p1
        

p1 = particle(0,1,1,1)

array = branch(p1, z(), theta())

