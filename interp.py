#!/usr/bin/python3

# 
# Useful interpolation functions in python.
# 

import numpy as np
import scipy.interpolate
from scipy.interpolate import RegularGridInterpolator

#
# y = f(x) 
#

def interp_1d(x,fx,x_desired):

    interp_func = scipy.interpolate.interp1d(x, fx)  

    return interp_func(x_desired)

#
# z = f(x,y)
#

def interp_2d(x,y,fxy,x_desired,y_desired):

    interp_func = scipy.interpolate.interp2d(x, y, fxy, kind='cubic')

    return interp_func(x_desired,y_desired)

#
# w = f(x,y,z)
#

def interp_3d(x,y,z,fxyz,x_desired,y_desired,z_desired):

    interp_func = RegularGridInterpolator((x,y,z), fxyz)

    return interp_func([x_desired,y_desired,z_desired])

#
# Main function.
#

def main():

    print("Checking interpolation 1-D")

    x  = [0.0,1.0,2.0,3.0]
    fx = [50.0,60.0,70.0,80.0]

    print(interp_1d(x,fx,0.5))

    x   =  np.array([0.0,1.0,2.0,3.0,4.0])
    y   =  np.array([0.0,1.0,2.0,3.0,4.0])
    fxy =  np.array([[50.0,60.0,70.0,80.0,100.0],
                     [50.0,60.0,70.0,80.0,100.0],
                     [50.0,60.0,70.0,80.0,100.0],
                     [50.0,60.0,70.0,80.0,100.0],
                     [50.0,60.0,70.0,80.0,100.0]])

    x_desired = 1.0
    y_desired = 1.0

    print(interp_2d(x,y,fxy,x_desired,y_desired))

    x    =  np.array([0.0,1.0,2.0,3.0])
    y    =  np.array([0.0,1.0,2.0,3.0])
    z    =  np.array([0.0,1.0,2.0,3.0])
    fxyz =  np.array([[[50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0]],
                     [[50.0,60.0,70.0,80.0],  
                      [50.0,60.0,70.0,80.0],  
                      [50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0]],
                     [[50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0]],
                     [[50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0],
                      [50.0,60.0,70.0,80.0]]])
    
    x_desired = 1.0
    y_desired = 1.0
    z_desired = 1.0

    print(interp_3d(x,y,z,fxyz,x_desired,y_desired,z_desired))
        
if __name__== "__main__":
    main()
