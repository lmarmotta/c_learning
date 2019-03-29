#!/usr/bin/python2

import numpy as np
from scipy.interpolate import griddata
from scipy.interpolate import Rbf

# Uses RBF function to interpolate.

def interp_rb(x,y,z,fxyz):
    return Rbf(x,y,z,fxyz,function='multiquadric') 

# Uses griddata to interpolate.

def interp_3d(data,x_desired,y_desired,z_desired):
    x, y, z, f = data.T
    return griddata(data[:, :3], f, (x_desired, y_desired, z_desired),method='nearest')

# Define the structures.

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

x = np.array([])
y = np.array([])
z = np.array([])
f = np.array([])

for i in xrange(12):
    x = np.append(x,data[i][0])
    y = np.append(y,data[i][1])
    z = np.append(z,data[i][2])
    f = np.append(f,data[i][3])

fxyz = interp_rb(x,y,z,f)

f_or = open("plot_gab.dat",'w')
f_rb = open("plot_rbf.dat",'w')
f_3d = open("plot_3ds.dat",'w')

print "------------------- Testing griddata ------------------- "

for i in xrange(12):
    interped = interp_3d(data,x[i], y[i], z[i])
    f_3d.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(interped) + "\n")
    print str(interped) + ' Delta = ' + str( (abs(interped)/abs(f[i]) - 1.0) * 100.0 ) + " [%]"

print "------------------- Testing RBF ------------------- "

for i in xrange(12):
    interped = fxyz(x[i], y[i], z[i])
    f_rb.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(interped) + "\n")
    print str(interped) + ' Delta = ' + str( (abs(interped)/abs(f[i]) - 1.0) * 100.0 ) + " [%]"

print "------------------- Write output file ------------------- "

for i in xrange(12):
    f_or.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(f[i]) + "\n")

f_rb.close()
f_3d.close()
f_or.close()
