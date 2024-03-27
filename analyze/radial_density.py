#! /usr/bin/env python

import numpy as np
from scipy import signal

def get_density(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, Rmax, increment):

  dis_R = np.arange(0, Rmax, increment)
  density = []
  for i in range(len(dis_R)):
    density_i = 0.0
    for j in range(len(orb_coeff)):
      for k in range(len(orb_coeff)):
        density_i = density_i+dis_R[i]**2*orb_coeff[j]*orb_norm_coeff[j]*orb_coeff[k]*orb_norm_coeff[k]*\
                    dis_R[i]**(n[j]+n[k]-2)*np.exp(-(tot_zeta[j]+tot_zeta[k])*dis_R[i])
    density.append(density_i*tot_norm**(-2))

  return dis_R, density

def find_density_peak(density):

  max_peak_index, _ = signal.find_peaks(density)
  min_peak_index, _ = signal.find_peaks([-x for x in density])

  return max_peak_index, min_peak_index

