#! /usr/bin/env python

import numpy as np
from astroutils.matplotlibrc import *

mpl.rcParams['font.size'] = 28
mpl.rcParams['xtick.major.pad']='6'

fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0.21, 0.15, 0.74, 0.8])

q = np.logspace(-2, 2)
r = (.49 * q**(2./3) / (.6 * q**(2./3) + np.log(1 + q**(1./3))) * (1 + q)**4
  / (16 * q**2))

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel(r'mass ratio')
ax.set_ylabel(r'$r_L / a_{\min}$')

ax.plot(q, r, c='k')

filename = 'roche_q'
dvires = 240
plt.savefig(filename + '.png', dpi=dvires, transparent=True)
