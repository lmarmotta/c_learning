#!/usr/bin/python2

import numpy as np
from scipy.interpolate import griddata

# Creates a grid over scatter data and interpolates a desired value.
# If you want to create an array from vectors use the procedure:
# data = np.array([])
# 
# for i in xrange(len(f)):
#     data = np.append(data,[x[i], y[i], z[i], f[i]])
# 
# data = data.reshape(len(f),4)


def interp_3d(data,x_desired,y_desired,z_desired):
    x, y, z, f = data.T
    return griddata(data[:, :3], f, (x_desired, y_desired, z_desired),method='nearest')

data = np.array([
        [2.66e+04, 5.00e+03, 5.00e-02, 0.01000],
        [2.66e+04, 5.00e+03, 1.00e-01, 0.02000],
        [2.66e+04, 5.00e+03, 1.50e-01, 0.03000],
        [2.66e+04, 5.00e+03, 2.00e-01, 0.04000],
        [2.66e+04, 5.00e+03, 2.50e-01, 0.05000],
        [2.66e+04, 1.00e+04, 5.00e-02, 0.06000],
        [2.66e+04, 1.00e+04, 1.00e-01, 0.07000],
        [2.66e+04, 1.00e+04, 1.50e-01, 0.08000],
        [2.66e+04, 1.00e+04, 2.00e-01, 0.09000],
        [4.00e+04, 5.00e+03, 0.00e+00, 0.10000],
        [4.00e+04, 5.00e+03, 5.00e-02, 0.11000],
        [4.00e+04, 5.00e+03, 1.00e-01, 0.12000],
        [4.00e+04, 5.00e+03, 1.50e-01, 0.13000]])

print interp_3d(data,4.00e+04,5.00e+03,5.00e-02)

