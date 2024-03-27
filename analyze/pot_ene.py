#! /usr/bin/env python

import math
import numpy as np
from scipy import signal
from AOPC.tools import numeric

def orb_pot(kin_R, E_tot_R):

  pot_R = []
  for i in range(len(E_tot_R)):
    pot_R.append(E_tot_R[i] - kin_R[i])

  return pot_R

def calc_pot_R_screen(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, dis_R, screen_R, atom_num):

  pot_R_screen = []
  int_part = 0

  dis_R.insert(0,0)

  for i in range(len(dis_R)-1):
    pot_sh_part = 0.0
    for j in range(len(orb_coeff)):
      for k in range(len(orb_coeff)):
        coeff = orb_coeff[j]*orb_norm_coeff[j]*orb_coeff[k]*orb_norm_coeff[k]
        n_tot = n[j]+n[k]
        a = tot_zeta[j]+tot_zeta[k]
        if n_tot == 2:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_1(a, dis_R[i+1])-numeric.int_gamma_1(a, dis_R[i]))
        if n_tot == 3:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_2(a, dis_R[i+1])-numeric.int_gamma_2(a, dis_R[i]))
        if n_tot == 4:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_3(a, dis_R[i+1])-numeric.int_gamma_3(a, dis_R[i]))
        if n_tot == 5:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_4(a, dis_R[i+1])-numeric.int_gamma_4(a, dis_R[i]))
        if n_tot == 6:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_5(a, dis_R[i+1])-numeric.int_gamma_5(a, dis_R[i]))
        if n_tot == 7:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_6(a, dis_R[i+1])-numeric.int_gamma_6(a, dis_R[i]))
        if n_tot == 8:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_7(a, dis_R[i+1])-numeric.int_gamma_7(a, dis_R[i]))
        if n_tot == 9:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_8(a, dis_R[i+1])-numeric.int_gamma_8(a, dis_R[i]))
        if n_tot == 10:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_9(a, dis_R[i+1])-numeric.int_gamma_9(a, dis_R[i]))
        if n_tot == 11:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_10(a, dis_R[i+1])-numeric.int_gamma_10(a, dis_R[i]))
        if n_tot == 12:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_11(a, dis_R[i+1])-numeric.int_gamma_11(a, dis_R[i]))
        if n_tot == 13:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_12(a, dis_R[i+1])-numeric.int_gamma_12(a, dis_R[i]))
        if n_tot == 14:
          pot_sh_part = pot_sh_part+coeff*(numeric.int_gamma_13(a, dis_R[i+1])-numeric.int_gamma_13(a, dis_R[i]))

    int_part = int_part+pot_sh_part*(screen_R[i]-atom_num)
    pot_R_screen.append(int_part)

  return pot_R_screen

def find_pot_plateau(pot_R, dis_R, increment, orb):

  pot_R_grad_org = np.gradient(pot_R)
  pot_R_grad = []
  for i in range(len(dis_R)):
    pot_R_grad.append(math.log(10)*dis_R[i]*pot_R_grad_org[i]/increment)
  max_peak_index, _ = signal.find_peaks(pot_R_grad)
  min_peak_index, _ = signal.find_peaks([-x for x in pot_R_grad])
  #pot_grad = pot_R_grad_org[min_peak_index[orb-1]]
  #for i in range(min_peak_index[orb-1], len(pot_R), 1):
  #  if ( abs(pot_R_grad_org[i]) < abs(pot_grad)/50.0 ):
  #    final_index = i
  #    break
  for i in range(min_peak_index[orb-1], len(pot_R), 1):
    if ( abs(pot_R[i]-pot_R[len(pot_R)-1]) < abs(pot_R[len(pot_R)-1])*0.001 ):
      final_index = i
      break
  peak_index = list(max_peak_index[0:(orb-1)])
  peak_index.append(final_index)

  return peak_index


