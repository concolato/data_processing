
import pandas as pd
import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt

from numpy.random import uniform, seed
from matplotlib.mlab import griddata
import numpy as np

def yahooRealEst():
	start = datetime.datetime(2010, 1, 1)
	end = datetime.datetime(2015, 1, 1)

	df = web.DataReader("XOM", "yahoo", start, end)

	print(df.head())

	df["Adj Close"].plot()

	plt.show() 

def testMatPlot():
	# make up data.
	#npts = int(raw_input('enter # of random points to plot:'))
	seed(0)
	npts = 200
	x = uniform(-2, 2, npts)
	y = uniform(-2, 2, npts)
	z = x*np.exp(-x**2 - y**2)
	# define grid.
	xi = np.linspace(-2.1, 2.1, 100)
	yi = np.linspace(-2.1, 2.1, 200)
	# grid the data.
	zi = griddata(x, y, z, xi, yi, interp='linear')
	# contour the gridded data, plotting dots at the nonuniform data points.
	CS = plt.contour(xi, yi, zi, 15, linewidths=0.5, colors='k')
	CS = plt.contourf(xi, yi, zi, 15, cmap=plt.cm.rainbow,
	                  vmax=abs(zi).max(), vmin=-abs(zi).max())
	plt.colorbar()  # draw colorbar
	# plot data points.
	plt.scatter(x, y, marker='o', c='b', s=5, zorder=10)
	plt.xlim(-2, 2)
	plt.ylim(-2, 2)
	plt.title('griddata test (%d points)' % npts)
	plt.show()

yahooRealEst()

testMatPlot()
