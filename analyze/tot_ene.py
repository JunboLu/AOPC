#! /usr/bin/env python

import numpy as np
from scipy import signal
from AOPC.analyze import integrate

def orb_tot(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, Rmax, increment, E):

  dis_R = np.arange(0, Rmax, increment)
  E_tot_R = []
  for i in range(len(dis_R)):
    E_tot = integrate.int_rR_2(dis_R[i], n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta)
    E_tot_R.append(E*E_tot)

  return dis_R, E_tot_R

def find_tot_plateau(tot_R, dis_R, increment, orb):

  tot_R_grad_org = np.gradient(tot_R)
  tot_R_grad = []
  for i in range(len(dis_R)):
    tot_R_grad.append(math.log(10)*dis_R[i]*tot_R_grad_org[i]/increment)
  max_peak_index, _ = signal.find_peaks(tot_R_grad)
  min_peak_index, _ = signal.find_peaks([-x for x in tot_R_grad])
  for i in range(min_peak_index[orb-1], len(tot_R), 1):
    if ( abs(tot_R[i]-tot_R[len(tot_R)-1]) < abs(tot_R[len(tot_R)-1])*0.001 ):
      final_index = i
      break
  peak_index = list(max_peak_index[0:(orb-1)])
  peak_index.append(final_index)

  return peak_index


