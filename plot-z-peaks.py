"""
Make various theory plots
"""
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# 0 os or 1 ss
type = 1

fig = plt.figure()
ax = fig.add_subplot(111)
if type ==0 : 
  filenames = ["data/z_peak_2charge_os.dat","data/z_peak_3charge_os.dat"]
else :
  filenames = ["data/z_peak_2charge_ss.dat","data/z_peak_3charge_ss.dat"]
colours = ["red","blue"]
markers = ["o","x"]
labels = ["GSF track charge","Unanimous charge"]

plots = []

for label,marker,colour,filename in zip(labels,markers,colours,filenames):
  file = open(filename,"r")
  x = []
  y = []
  for line in file:
      data = line.split(",")
      if data != [] : 
        x.append(round(float(data[0])-0.5)+0.5) # round to nearest 0.5
        y.append(round(float(data[1])))
  yerr = np.sqrt(y)
  l = ax.errorbar(x, y, xerr=0.5, yerr=yerr, color=colour, fmt=marker, ms=5., label=label)
  plots.append(l)

ax.legend( loc='upper left', numpoints = 1 )

if type ==0 : 
  ax.set_xlabel(r'$m_{e^{\pm}e^{\mp}}~(GeV)$')
else:
  ax.set_xlabel(r'$m_{e^{\pm}e^{\pm}}~(GeV)$')
ax.set_ylabel(r'Events/GeV')
ax.set_ylim(0)
ax.set_xlim(60,120)
ax.grid(True)

plt.show()

