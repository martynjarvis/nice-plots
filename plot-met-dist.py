"""
Make various theory plots
"""
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#filename = "data/met_dist_36pb.dat"
filename = "data/met_dist_840pb.dat"

fig = plt.figure()
ax = fig.add_subplot(111)

file = open(filename,"r")
x = []
y = []
for line in file:
  data = line.split(",")
  if data != [] : 
    x.append(round(float(data[0])-0.5)+0.5) # round to nearest 0.5
    y.append(float(data[1]))

yerr = np.sqrt(y)
#l = ax.plot(x, y, fmt="x", ms=5.)
l = ax.step(x, y,where='mid')


ax.set_xlabel(r'Particle Flow $E_T^{miss}$~(GeV)')
ax.set_ylabel(r'Events/GeV')
ax.set_ylim(0)
#ax.set_xlim(60,120)
#ax.grid(True) # NOPE

plt.show()

