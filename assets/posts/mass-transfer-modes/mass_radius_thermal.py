#! /usr/bin/env python

import numpy as np
from astroutils.matplotlibrc import *
from roche_q import calc_qr

if __name__ == '__main__':
  mpl.rcParams['font.size'] = 28
  mpl.rcParams['xtick.major.pad']='6'

  fig = plt.figure(figsize=(6, 6))
  ax = fig.add_axes([0.21, 0.15, 0.74, 0.8])

  ax.set_xscale('log')
  ax.set_yscale('log')
  ax.set_xlabel(r'mass ratio')
  ax.set_ylabel(r'$r_L / a_{\min}$')

  # Plot the Roche-lobe radius
  q, r = calc_qr()
  ax.plot(q, r, c='k')

  # Plot the initial mass-radius relationship
  X0 = np.linspace(1.1, 1.8)
  Y0 = 4 * X0 
