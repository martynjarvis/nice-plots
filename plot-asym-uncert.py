"""
Make various theory plots
"""

from matplotlib import rc
#rcParams.update({'font.size': 16})
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
font = {'family' : 'normal',
        'size'   : 16}
rc('font', **font)
rc('text', usetex=True)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

fig = plt.figure()
ax = fig.add_subplot(111)

#filenames = ["data/asym_mstw.dat","data/asym_ct10w.dat"]
filenames = ["data/asym_mstw_30.dat","data/asym_ct10w_30.dat"]
colours = ["blue","red"]
styles = ["b--","r-"]
labels = ["MSTW2008NLO","CT10W"]

for filename,colour,style,label in zip(filenames,colours,styles,labels):
  file = open(filename,"r")
  x = []
  y = []
  yerrp = []
  yerrm = []
  
  
  for line in file:
    data = line.split(",")
    if data != [] : 
      #print data
      x.append(float(data[0]))
      y.append(float(data[1]))
      yerrp.append(float(data[2]))
      yerrm.append(float(data[3]))
  l = plt.plot(x, y, style, label=label)
  e = plt.fill_between(x, np.subtract(y,yerrm), np.add(y,yerrp),alpha=0.3,color=colour)

ax.set_ylim(0, 0.4)

plt.text(0.2, 0.375, r'$pp\to W+X \to e \nu + X$', size=14)
plt.text(0.2, 0.3375, r'$\sqrt{s}=7\ TeV$', size=14)

plt.text(2.2, 0.025, r'$P^{e}_{T} > 30\ GeV$', size=14)
#plt.text(2.2, 0.025, r'$\eta^{e}<3.0$', size=14)

lg = ax.legend( loc='upper right', numpoints = 1 ,prop={'size':14})
lg.get_frame().set_linewidth(0)

ax.set_xlabel(r'$\eta_e$')
ax.set_ylabel(r'$\mathcal{A}(\eta_e)$')

plt.show()
