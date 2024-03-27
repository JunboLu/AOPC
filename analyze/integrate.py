#! /usr/bin/env python

import numpy as np
from scipy import integrate
from AOPC.tools import numeric

def int_R_2(rm, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta):

  int_value = 0.0

  for i in range(len(orb_coeff)):
    for j in range(len(orb_coeff)):
      coeff = orb_coeff[i]*orb_norm_coeff[i]*orb_coeff[j]*orb_norm_coeff[j]
      n_tot = n[i]+n[j]
      a = tot_zeta[i]+tot_zeta[j]
      int_gamma_0_0 = numeric.int_gamma_0(a, 0)
      int_gamma_1_0 = numeric.int_gamma_1(a, 0)
      int_gamma_2_0 = numeric.int_gamma_2(a, 0)
      int_gamma_3_0 = numeric.int_gamma_3(a, 0)
      int_gamma_4_0 = numeric.int_gamma_4(a, 0)
      int_gamma_5_0 = numeric.int_gamma_5(a, 0)
      int_gamma_6_0 = numeric.int_gamma_6(a, 0)
      int_gamma_7_0 = numeric.int_gamma_7(a, 0)
      int_gamma_8_0 = numeric.int_gamma_8(a, 0)
      int_gamma_9_0 = numeric.int_gamma_9(a, 0)
      int_gamma_10_0 = numeric.int_gamma_10(a, 0)
      int_gamma_11_0 = numeric.int_gamma_11(a, 0)
      int_gamma_12_0 = numeric.int_gamma_12(a, 0)
      if n_tot == 2:
        int_value = int_value+coeff*(numeric.int_gamma_0(a, rm)-int_gamma_0_0)
      if n_tot == 3:
        int_value = int_value+coeff*(numeric.int_gamma_1(a, rm)-int_gamma_1_0)
      if n_tot == 4:
        int_value = int_value+coeff*(numeric.int_gamma_2(a, rm)-int_gamma_2_0)
      if n_tot == 5:
        int_value = int_value+coeff*(numeric.int_gamma_3(a, rm)-int_gamma_3_0)
      if n_tot == 6:
        int_value = int_value+coeff*(numeric.int_gamma_4(a, rm)-int_gamma_4_0)
      if n_tot == 7:
        int_value = int_value+coeff*(numeric.int_gamma_5(a, rm)-int_gamma_5_0)
      if n_tot == 8:
        int_value = int_value+coeff*(numeric.int_gamma_6(a, rm)-int_gamma_6_0)
      if n_tot == 9:
        int_value = int_value+coeff*(numeric.int_gamma_7(a, rm)-int_gamma_7_0)
      if n_tot == 10:
        int_value = int_value+coeff*(numeric.int_gamma_8(a, rm)-int_gamma_8_0)
      if n_tot == 11:
        int_value = int_value+coeff*(numeric.int_gamma_9(a, rm)-int_gamma_9_0)
      if n_tot == 12:
        int_value = int_value+coeff*(numeric.int_gamma_10(a, rm)-int_gamma_10_0)
      if n_tot == 13:
        int_value = int_value+coeff*(numeric.int_gamma_11(a, rm)-int_gamma_11_0)
      if n_tot == 14:
        int_value = int_value+coeff*(numeric.int_gamma_12(a, rm)-int_gamma_12_0)

  int_value = tot_norm**(-2)*int_value

  return int_value

def int_rR_2(rm, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta):

  int_value = 0.0

  for i in range(len(orb_coeff)):
    for j in range(len(orb_coeff)):
      coeff = orb_coeff[i]*orb_norm_coeff[i]*orb_coeff[j]*orb_norm_coeff[j]
      n_tot = n[i]+n[j]
      a = tot_zeta[i]+tot_zeta[j]
      int_gamma_2_0 = numeric.int_gamma_2(a, 0)
      int_gamma_3_0 = numeric.int_gamma_3(a, 0)
      int_gamma_4_0 = numeric.int_gamma_4(a, 0)
      int_gamma_5_0 = numeric.int_gamma_5(a, 0)
      int_gamma_6_0 = numeric.int_gamma_6(a, 0)
      int_gamma_7_0 = numeric.int_gamma_7(a, 0)
      int_gamma_8_0 = numeric.int_gamma_8(a, 0)
      int_gamma_9_0 = numeric.int_gamma_9(a, 0)
      int_gamma_10_0 = numeric.int_gamma_10(a, 0)
      int_gamma_11_0 = numeric.int_gamma_11(a, 0)
      int_gamma_12_0 = numeric.int_gamma_12(a, 0)
      int_gamma_13_0 = numeric.int_gamma_13(a, 0)
      int_gamma_14_0 = numeric.int_gamma_14(a, 0)
      if n_tot == 2:
        int_value = int_value+coeff*(numeric.int_gamma_2(a, rm)-int_gamma_2_0)
      if n_tot == 3:
        int_value = int_value+coeff*(numeric.int_gamma_3(a, rm)-int_gamma_3_0)
      if n_tot == 4:
        int_value = int_value+coeff*(numeric.int_gamma_4(a, rm)-int_gamma_4_0)
      if n_tot == 5:
        int_value = int_value+coeff*(numeric.int_gamma_5(a, rm)-int_gamma_5_0)
      if n_tot == 6:
        int_value = int_value+coeff*(numeric.int_gamma_6(a, rm)-int_gamma_6_0)
      if n_tot == 7:
        int_value = int_value+coeff*(numeric.int_gamma_7(a, rm)-int_gamma_7_0)
      if n_tot == 8:
        int_value = int_value+coeff*(numeric.int_gamma_8(a, rm)-int_gamma_8_0)
      if n_tot == 9:
        int_value = int_value+coeff*(numeric.int_gamma_9(a, rm)-int_gamma_9_0)
      if n_tot == 10:
        int_value = int_value+coeff*(numeric.int_gamma_10(a, rm)-int_gamma_10_0)
      if n_tot == 11:
        int_value = int_value+coeff*(numeric.int_gamma_11(a, rm)-int_gamma_11_0)
      if n_tot == 12:
        int_value = int_value+coeff*(numeric.int_gamma_12(a, rm)-int_gamma_12_0)
      if n_tot == 13:
        int_value = int_value+coeff*(numeric.int_gamma_13(a, rm)-int_gamma_13_0)
      if n_tot == 14:
        int_value = int_value+coeff*(numeric.int_gamma_14(a, rm)-int_gamma_14_0)

  int_value = tot_norm**(-2)*int_value

  return int_value

def int_rdRdr_2(rm, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta):

  int_value = 0.0

  for i in range(len(orb_coeff)):
    for j in range(len(orb_coeff)):
      coeff = orb_coeff[i]*orb_norm_coeff[i]*orb_coeff[j]*orb_norm_coeff[j]
      n_tot = n[i]+n[j]
      a = tot_zeta[i]+tot_zeta[j]
      int_gamma_0_0 = numeric.int_gamma_0(a, 0)
      int_gamma_1_0 = numeric.int_gamma_1(a, 0)
      int_gamma_2_0 = numeric.int_gamma_2(a, 0)
      int_gamma_3_0 = numeric.int_gamma_3(a, 0)
      int_gamma_4_0 = numeric.int_gamma_4(a, 0)
      int_gamma_5_0 = numeric.int_gamma_5(a, 0)
      int_gamma_6_0 = numeric.int_gamma_6(a, 0)
      int_gamma_7_0 = numeric.int_gamma_7(a, 0)
      int_gamma_8_0 = numeric.int_gamma_8(a, 0)
      int_gamma_9_0 = numeric.int_gamma_9(a, 0)
      int_gamma_10_0 = numeric.int_gamma_10(a, 0)
      int_gamma_11_0 = numeric.int_gamma_11(a, 0)
      int_gamma_12_0 = numeric.int_gamma_12(a, 0)
      int_gamma_13_0 = numeric.int_gamma_13(a, 0)
      int_gamma_14_0 = numeric.int_gamma_14(a, 0)
      if n_tot == 2:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_0(a, rm)-int_gamma_0_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_1(a, rm)-int_gamma_1_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_1(a, rm)-int_gamma_1_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_2(a, rm)-int_gamma_2_0)
      if n_tot == 3:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_1(a, rm)-int_gamma_1_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_2(a, rm)-int_gamma_2_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_2(a, rm)-int_gamma_2_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_3(a, rm)-int_gamma_3_0)
      if n_tot == 4:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_2(a, rm)-int_gamma_2_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_3(a, rm)-int_gamma_3_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_3(a, rm)-int_gamma_3_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_4(a, rm)-int_gamma_4_0)
      if n_tot == 5:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_3(a, rm)-int_gamma_3_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_4(a, rm)-int_gamma_4_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_4(a, rm)-int_gamma_4_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_5(a, rm)-int_gamma_5_0)
      if n_tot == 6:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_4(a, rm)-int_gamma_4_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_5(a, rm)-int_gamma_5_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_5(a, rm)-int_gamma_5_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_6(a, rm)-int_gamma_6_0)
      if n_tot == 7:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_5(a, rm)-int_gamma_5_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_6(a, rm)-int_gamma_6_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_6(a, rm)-int_gamma_6_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_7(a, rm)-int_gamma_7_0)
      if n_tot == 8:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_6(a, rm)-int_gamma_6_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_7(a, rm)-int_gamma_7_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_7(a, rm)-int_gamma_7_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_8(a, rm)-int_gamma_8_0)
      if n_tot == 9:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_7(a, rm)-int_gamma_7_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_8(a, rm)-int_gamma_8_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_8(a, rm)-int_gamma_8_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_9(a, rm)-int_gamma_9_0)
      if n_tot == 10:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_8(a, rm)-int_gamma_8_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_9(a, rm)-int_gamma_9_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_9(a, rm)-int_gamma_9_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_10(a, rm)-int_gamma_10_0)
      if n_tot == 11:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_9(a, rm)-int_gamma_9_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_10(a, rm)-int_gamma_10_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_10(a, rm)-int_gamma_10_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_11(a, rm)-int_gamma_11_0)
      if n_tot == 12:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_10(a, rm)-int_gamma_10_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_11(a, rm)-int_gamma_11_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_11(a, rm)-int_gamma_11_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_12(a, rm)-int_gamma_12_0)
      if n_tot == 13:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_11(a, rm)-int_gamma_11_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_12(a, rm)-int_gamma_12_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_12(a, rm)-int_gamma_12_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_13(a, rm)-int_gamma_13_0)
      if n_tot == 14:
        int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*(numeric.int_gamma_12(a, rm)-int_gamma_12_0) - \
                 coeff*(n[i]-1)*tot_zeta[j]*(numeric.int_gamma_13(a, rm)-int_gamma_13_0) - \
                 coeff*(n[j]-1)*tot_zeta[i]*(numeric.int_gamma_13(a, rm)-int_gamma_13_0) + \
                 coeff*tot_zeta[i]*tot_zeta[j]*(numeric.int_gamma_14(a, rm)-int_gamma_14_0)
      if n_tot > 14:
        print ("We do not consider n>14, please add integration of new gamma function.", flush=True)
        exit()

  int_value = tot_norm**(-2)*int_value

  return int_value

def int_r_3_R_2(rm, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta):

  int_value = 0.0

  for i in range(len(orb_coeff)):
    for j in range(len(orb_coeff)):
      coeff = orb_coeff[i]*orb_norm_coeff[i]*orb_coeff[j]*orb_norm_coeff[j]
      n_tot = n[i]+n[j]
      a = tot_zeta[i]+tot_zeta[j]
      int_gamma_3_0 = numeric.int_gamma_3(a, 0)
      int_gamma_4_0 = numeric.int_gamma_4(a, 0)
      int_gamma_5_0 = numeric.int_gamma_5(a, 0)
      int_gamma_6_0 = numeric.int_gamma_6(a, 0)
      int_gamma_7_0 = numeric.int_gamma_7(a, 0)
      int_gamma_8_0 = numeric.int_gamma_8(a, 0)
      int_gamma_9_0 = numeric.int_gamma_9(a, 0)
      int_gamma_10_0 = numeric.int_gamma_10(a, 0)
      int_gamma_11_0 = numeric.int_gamma_11(a, 0)
      int_gamma_12_0 = numeric.int_gamma_12(a, 0)
      int_gamma_13_0 = numeric.int_gamma_13(a, 0)
      int_gamma_14_0 = numeric.int_gamma_14(a, 0)
      int_gamma_15_0 = numeric.int_gamma_15(a, 0)
      if n_tot == 2:
        int_value = int_value+coeff*(numeric.int_gamma_3(a, rm)-int_gamma_3_0)
      if n_tot == 3:
        int_value = int_value+coeff*(numeric.int_gamma_4(a, rm)-int_gamma_4_0)
      if n_tot == 4:
        int_value = int_value+coeff*(numeric.int_gamma_5(a, rm)-int_gamma_5_0)
      if n_tot == 5:
        int_value = int_value+coeff*(numeric.int_gamma_6(a, rm)-int_gamma_6_0)
      if n_tot == 6:
        int_value = int_value+coeff*(numeric.int_gamma_7(a, rm)-int_gamma_7_0)
      if n_tot == 7:
        int_value = int_value+coeff*(numeric.int_gamma_8(a, rm)-int_gamma_8_0)
      if n_tot == 8:
        int_value = int_value+coeff*(numeric.int_gamma_9(a, rm)-int_gamma_9_0)
      if n_tot == 9:
        int_value = int_value+coeff*(numeric.int_gamma_10(a, rm)-int_gamma_10_0)
      if n_tot == 10:
        int_value = int_value+coeff*(numeric.int_gamma_11(a, rm)-int_gamma_11_0)
      if n_tot == 11:
        int_value = int_value+coeff*(numeric.int_gamma_12(a, rm)-int_gamma_12_0)
      if n_tot == 12:
        int_value = int_value+coeff*(numeric.int_gamma_13(a, rm)-int_gamma_13_0)
      if n_tot == 13:
        int_value = int_value+coeff*(numeric.int_gamma_14(a, rm)-int_gamma_14_0)
      if n_tot == 14:
        int_value = int_value+coeff*(numeric.int_gamma_15(a, rm)-int_gamma_15_0)

  int_value = tot_norm**(-2)*int_value

  return int_value

def int_r_4_R_2(rm, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta):

  int_value = 0.0

  for i in range(len(orb_coeff)):
    for j in range(len(orb_coeff)):
      coeff = orb_coeff[i]*orb_norm_coeff[i]*orb_coeff[j]*orb_norm_coeff[j]
      n_tot = n[i]+n[j]
      a = tot_zeta[i]+tot_zeta[j]
      int_gamma_4_0 = numeric.int_gamma_4(a, 0)
      int_gamma_5_0 = numeric.int_gamma_5(a, 0)
      int_gamma_6_0 = numeric.int_gamma_6(a, 0)
      int_gamma_7_0 = numeric.int_gamma_7(a, 0)
      int_gamma_8_0 = numeric.int_gamma_8(a, 0)
      int_gamma_9_0 = numeric.int_gamma_9(a, 0)
      int_gamma_10_0 = numeric.int_gamma_10(a, 0)
      int_gamma_11_0 = numeric.int_gamma_11(a, 0)
      int_gamma_12_0 = numeric.int_gamma_12(a, 0)
      int_gamma_13_0 = numeric.int_gamma_13(a, 0)
      int_gamma_14_0 = numeric.int_gamma_14(a, 0)
      int_gamma_15_0 = numeric.int_gamma_15(a, 0)
      int_gamma_16_0 = numeric.int_gamma_16(a, 0)
      if n_tot == 2:
        int_value = int_value+coeff*(numeric.int_gamma_4(a, rm)-int_gamma_4_0)
      if n_tot == 3:
        int_value = int_value+coeff*(numeric.int_gamma_5(a, rm)-int_gamma_5_0)
      if n_tot == 4:
        int_value = int_value+coeff*(numeric.int_gamma_6(a, rm)-int_gamma_6_0)
      if n_tot == 5:
        int_value = int_value+coeff*(numeric.int_gamma_7(a, rm)-int_gamma_7_0)
      if n_tot == 6:
        int_value = int_value+coeff*(numeric.int_gamma_8(a, rm)-int_gamma_8_0)
      if n_tot == 7:
        int_value = int_value+coeff*(numeric.int_gamma_9(a, rm)-int_gamma_9_0)
      if n_tot == 8:
        int_value = int_value+coeff*(numeric.int_gamma_10(a, rm)-int_gamma_10_0)
      if n_tot == 9:
        int_value = int_value+coeff*(numeric.int_gamma_11(a, rm)-int_gamma_11_0)
      if n_tot == 10:
        int_value = int_value+coeff*(numeric.int_gamma_12(a, rm)-int_gamma_12_0)
      if n_tot == 11:
        int_value = int_value+coeff*(numeric.int_gamma_13(a, rm)-int_gamma_13_0)
      if n_tot == 12:
        int_value = int_value+coeff*(numeric.int_gamma_14(a, rm)-int_gamma_14_0)
      if n_tot == 13:
        int_value = int_value+coeff*(numeric.int_gamma_15(a, rm)-int_gamma_15_0)
      if n_tot == 14:
        int_value = int_value+coeff*(numeric.int_gamma_16(a, rm)-int_gamma_16_0)

  int_value = tot_norm**(-2)*int_value

  return int_value

def int_zora_R_2(r, f1, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta):

  int_value = 0.0

  for i in range(len(orb_coeff)):
    for j in range(len(orb_coeff)):
      coeff = orb_coeff[i]*orb_norm_coeff[i]*orb_coeff[j]*orb_norm_coeff[j]
      n_tot = n[i]+n[j]
      a = tot_zeta[i]+tot_zeta[j]
      f2 = []
      for k in range(len(r)):
        f2.append(r[k]**(n_tot-2)*np.exp(-a*r[k]))
      f_int_1 = []
      for k in range(len(r)):
        f_int_1.append(f1[k]*f2[k])

      int_value = int_value+coeff*integrate.trapz(f_int_1, r)

  int_value = tot_norm**(-2)*int_value

  return int_value

def int_zora_rdRdr_2(r, f1, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta):

  int_value = 0.0

  for i in range(len(orb_coeff)):
    for j in range(len(orb_coeff)):
      coeff = orb_coeff[i]*orb_norm_coeff[i]*orb_coeff[j]*orb_norm_coeff[j]
      n_tot = n[i]+n[j]
      a = tot_zeta[i]+tot_zeta[j]
      f2 = []
      for k in range(len(r)):
        f2.append(r[k]**(n_tot-2)*np.exp(-a*r[k]))
      f_int_1 = []
      for k in range(len(r)):
        f_int_1.append(f1[k]*f2[k])
      f2 = []
      for k in range(len(r)):
        f2.append(r[k]**(n_tot-1)*np.exp(-a*r[k]))
      f_int_2 = []
      for k in range(len(r)):
        f_int_2.append(f1[k]*f2[k])
      f2 = []
      for k in range(len(r)):
        f2.append(r[k]**(n_tot)*np.exp(-a*r[k]))
      f_int_3 = []
      for l in range(len(r)):
        f_int_3.append(f1[k]*f2[k])
      int_value = int_value+coeff*(n[i]-1)*(n[j]-1)*integrate.trapz(f_int_1, r) - \
               2*coeff*(n[i]-1)*tot_zeta[j]*integrate.trapz(f_int_2, r) + \
               coeff*tot_zeta[i]*tot_zeta[j]*integrate.trapz(f_int_3, r)

  int_value = tot_norm**(-2)*int_value

  return int_value

