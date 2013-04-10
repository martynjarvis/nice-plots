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

filenames = ["../MCFM/Bin/MSTW2008nlo68cl_wp/W_only_tota_MSTW200_80__80__test.dat", 
             "../MCFM/Bin/MSTW2008nlo68cl_wm/W_only_tota_MSTW200_80__80__test.dat"]
labels = ["$e^{+}$","$e^{-}$"]

xs = []
ys = []
for filename in filenames :
  x = []
  y = []

  file = open(filename,'r')
  w_rap_start = False 

  for line in file:
    if w_rap_start:
      data = line.split()
      if data == [] : 
        w_rap_start=False
      else :
        x.append(float(data[0]))
        y.append(float(data[1])*0.001*1.0)
    if "y(lep)" in line:
      w_rap_start = True
  xs.append(x)
  ys.append(y)

#for i,j in zip(x,y):
# print i,j


# plot it
fig = plt.figure()
ax = fig.add_subplot(111)
ls = []
for label,x,y in zip(labels,xs,ys):
  #l = ax.plot(x, y, linewidth=1)
  l = ax.step(x, y, where='mid', label=label, lw=1)
  ls.append(l)

plt.text(-2.7, 750., r'$pp\to W+X \to e \nu + X$', size=14)
plt.text(-2.7, 700., r'$\sqrt{s}=7\ TeV$', size=14)

plt.text(-2.7, 100., r'$P^{e}_{T} > 25\ GeV$', size=14)
plt.text(-2.7, 50., r'$\eta^{e}<3.0$', size=14)

lg = ax.legend( loc='lower right', numpoints = 1 ,prop={'size':16})
lg.get_frame().set_linewidth(0)

ax.set_xlabel(r'$\eta_e$')
ax.set_ylabel(r'$d\sigma/d\eta_{e}$ (pb)')
#ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
ax.set_xlim(-3, +3)
ax.set_ylim(0, +800)
#ax.set_ylim(0, 0.03)
#ax.grid(True)

plt.show()
