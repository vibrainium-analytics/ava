# Import statements
import numpy as np                  # Numpy handles numbers
import matplotlib.pyplot as pl      #Gnuplot in Matplotlib package

# Get data from file
data1 = np.loadtxt("car X.txt")
data2 = np.loadtxt("car Y.txt")

# Read data from file

# Setup subplots
pl.subplot(2,1,1)
pl.plot(data1[:,0], data1[:,1], "r*")
pl.title("Car X")
pl.xlabel("x")
pl.ylabel("y")
pl.xlim(0.0, 10.)
pl.ylim(0.0, 8.)

pl.subplot(2,1,2)
pl.plot(data2[:,0], data2[:,1], "r*")
pl.title("Car Y")
pl.xlabel("x")
pl.ylabel("y")
pl.xlim(0.0, 10.)
pl.ylim(0.0, 8.)

# Show plot(s)
pl.show()
