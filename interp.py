#!/usr/bin/python3

# 
# Useful interpolation functions in python.
# 

import numpy as np
import scipy.interpolate

#
# Linear interpolation is like making a function from a simple
# table of lines. Like searching for values in y = f(x).
#

def interp_1d(x,fx,x_desired):
    interp_func = scipy.interpolate.interp1d(x, fx)  
    return interp_func(x_desired)

#
# Interpolation in 2-D is like a graph with multiple isolines.
# You want to get a give value at a given line. 
# z = f(x,y)
#

def interp_2d(x,y,fxy,x_desired,y_desired):

    interp_func = scipy.interpolate.interp2d(x, y, fxy, kind='cubic')

    return interp_func(x_desired,y_desired)

#
# Main function.
#

def main():

    print("Checking interpolation 1-D")

    x  = [0.0,1.0,2.0,3.0]
    fx = [50.0,60.0,70.0,80.0]

    print("Desired value = " + str(55.0) + " | Obtained value = " + str(interp_1d(x,fx,0.5)))

    x   =  np.array([0.0,1.0,2.0,3.0,4.0])
    y   =  np.array([0.0,1.0,2.0,3.0,4.0])
    fxy =  np.array([[50.0,60.0,70.0,80.0,100.0],
                     [50.0,60.0,70.0,80.0,100.0],
                     [50.0,60.0,70.0,80.0,100.0],
                     [50.0,60.0,70.0,80.0,100.0],
                     [50.0,60.0,70.0,80.0,100.0]])

    x_desired = 1.0
    y_desired = 1.0

    print(interp_2d(x,y,fxy,x_desired,y_desired)[0])
    
        
if __name__== "__main__":
    main()
