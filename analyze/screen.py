#! /usr/bin/env python

from scipy import signal
from AOPC.tools import numeric

def calc_screen(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, dis_R, pot_R, final_plat, Z):

  screen_R = []
  final_dis_R = []
  final_pot_R = []
  for i in range(len(dis_R)-1):
    pot_sh_part = 0.0
    func_value = 0.0
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

    if ( pot_sh_part > 0 ):
      z_screen = (pot_R[i+1]-pot_R[i])/(pot_sh_part)
      screen_R.append(z_screen+Z)
      final_dis_R.append(dis_R[i+1])
      final_pot_R.append(pot_R[i+1])
      #print (dis_R[i+1], z_screen+Z, pot_R[i+1]-pot_R[i], pot_sh_part)
  return screen_R, final_dis_R, final_pot_R

def eval_final_screen(density_R, screen_R, dis_R, final_dis_R):

  screen = 0.0
  density = 0.0

  for j in range(len(dis_R)):
    if dis_R[j] in final_dis_R:
      screen_index = final_dis_R.index(dis_R[j])
      screen = screen+screen_R[screen_index]*density_R[j]
      density = density+density_R[j]

  final_screen = screen/density

  return final_screen
