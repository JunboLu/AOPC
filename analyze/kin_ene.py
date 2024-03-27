#! /usr/bin/env python

import math
import numpy as np
from scipy import signal
from AOPC.tools import call
from AOPC.tools import data_op
from AOPC.lib import fast_int_mod
from AOPC.analyze import integrate
from AOPC.analyze import veff_info

def grep_zora(work_dir, output):

  cmd = "grep %s %s" % ("'Relativistic Corrections:'", output)
  relat = call.call_returns_shell(work_dir, cmd)
  if 'ZORA' in relat[0]:
    ZORA=True
  else:
    ZORA=False

  return ZORA

def get_res_dir(work_dir, output):

  cmd = "grep %s %s" % ("'Results directory:'", output)
  line = call.call_returns_shell(work_dir, cmd)
  line_split = data_op.split_str(line[0], ' ', '\n')

  res_dir = line_split[2]

  return res_dir

def orb_s_kin(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, Rmax, increment, output, work_dir, atom, orb):

  dis_R = np.arange(0, Rmax, increment)
  kin_R = []
  ZORA = grep_zora(work_dir, output)
  if ZORA:
    res_dir = get_res_dir(work_dir, output)
    res_file = ''.join((res_dir, 'adf.rkf'))
    inter_r, f1 = veff_info.kernel(work_dir, res_file, atom, orb)
    kin_R.append(0.0)
    kin = fast_int_mod.fast_int.int_zora_rdrdr_2(np.asfortranarray(inter_r, dtype='float32'), \
                                                 np.asfortranarray(f1, dtype='float32'), \
                                                 np.asfortranarray(n, dtype='int32'), \
                                                 np.asfortranarray(orb_coeff, dtype='float32'), \
                                                 np.asfortranarray(orb_norm_coeff, dtype='float32'), tot_norm, \
                                                 np.asfortranarray(tot_zeta, dtype='float32'))
    for i in range(len(kin)):
      kin_R.append(0.5*kin[i])
  else:
    for i in range(len(dis_R)):
      kin = 0.5*integrate.int_rdRdr_2(dis_R[i], n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta)
      kin_R.append(kin)

  return dis_R, kin_R

def orb_p_kin(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, Rmax, increment, output, work_dir, atom, orb):

  dis_R = np.arange(0, Rmax, increment)
  kin_R = []
  ZORA = grep_zora(work_dir, output)
  if ZORA:
    res_dir = get_res_dir(work_dir, output)
    res_file = ''.join((res_dir, 'adf.rkf'))
    inter_r, f1 = veff_info.kernel(work_dir, res_file, atom, orb)
    kin_R.append(0.0)
    kin_1 = fast_int_mod.fast_int.int_zora_rdrdr_2(np.asfortranarray(inter_r, dtype='float32'), \
                                                   np.asfortranarray(f1, dtype='float32'), \
                                                   np.asfortranarray(n, dtype='int32'), \
                                                   np.asfortranarray(orb_coeff, dtype='float32'), \
                                                   np.asfortranarray(orb_norm_coeff, dtype='float32'), tot_norm, \
                                                   np.asfortranarray(tot_zeta, dtype='float32'))
    kin_2 = fast_int_mod.fast_int.int_zora_r_2(np.asfortranarray(inter_r, dtype='float32'), \
                                               np.asfortranarray(f1, dtype='float32'), \
                                               np.asfortranarray(n, dtype='int32'), \
                                               np.asfortranarray(orb_coeff, dtype='float32'), \
                                               np.asfortranarray(orb_norm_coeff, dtype='float32'), tot_norm, \
                                               np.asfortranarray(tot_zeta, dtype='float32'))
    for i in range(len(kin_1)):
      kin_R.append(0.5*kin_1[i]+1.0*kin_2[i])
  else:
    for i in range(len(dis_R)):
      kin = 0.5*integrate.int_rdRdr_2(dis_R[i], n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta) + \
            1.0*integrate.int_R_2(dis_R[i], n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta)
      kin_R.append(kin)

  return dis_R, kin_R

def orb_d_kin(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, Rmax, increment, output, work_dir, atom, orb):

  dis_R = np.arange(0, Rmax, increment)
  kin_R = []
  ZORA = grep_zora(work_dir, output)
  if ZORA:
    res_dir = get_res_dir(work_dir, output)
    res_file = ''.join((res_dir, 'adf.rkf'))
    inter_r, f1 = veff_info.kernel(work_dir, res_file, atom, orb)
    kin_R.append(0.0)
    kin_1 = fast_int_mod.fast_int.int_zora_rdrdr_2(np.asfortranarray(inter_r, dtype='float32'), \
                                                   np.asfortranarray(f1, dtype='float32'), \
                                                   np.asfortranarray(n, dtype='int32'), \
                                                   np.asfortranarray(orb_coeff, dtype='float32'), \
                                                   np.asfortranarray(orb_norm_coeff, dtype='float32'), tot_norm, \
                                                   np.asfortranarray(tot_zeta, dtype='float32'))
    kin_2 = fast_int_mod.fast_int.int_zora_r_2(np.asfortranarray(inter_r, dtype='float32'), \
                                               np.asfortranarray(f1, dtype='float32'), \
                                               np.asfortranarray(n, dtype='int32'), \
                                               np.asfortranarray(orb_coeff, dtype='float32'), \
                                               np.asfortranarray(orb_norm_coeff, dtype='float32'), tot_norm, \
                                               np.asfortranarray(tot_zeta, dtype='float32')) 
    for i in range(len(kin_1)):
      kin_R.append(0.5*kin_1[i]+3.0*kin_2[i])
  else:
    for i in range(len(dis_R)):
      kin = 0.5*integrate.int_rdRdr_2(dis_R[i], n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta) + \
            3.0*integrate.int_R_2(dis_R[i], n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta)
      kin_R.append(kin)

  return dis_R, kin_R

def orb_f_kin(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, Rmax, increment, output, work_dir, atom, orb):

  dis_R = np.arange(0, Rmax, increment)
  kin_R = []
  ZORA = grep_zora(work_dir, output)
  if ZORA:
    res_dir = get_res_dir(work_dir, output)
    res_file = ''.join((res_dir, 'adf.rkf'))
    inter_r, f1 = veff_info.kernel(work_dir, res_file, atom, orb)
    kin_R.append(0.0)
    kin_1 = fast_int_mod.fast_int.int_zora_rdrdr_2(np.asfortranarray(inter_r, dtype='float32'), \
                                                   np.asfortranarray(f1, dtype='float32'), \
                                                   np.asfortranarray(n, dtype='int32'), \
                                                   np.asfortranarray(orb_coeff, dtype='float32'), \
                                                   np.asfortranarray(orb_norm_coeff, dtype='float32'), tot_norm, \
                                                   np.asfortranarray(tot_zeta, dtype='float32'))
    kin_2 = fast_int_mod.fast_int.int_zora_r_2(np.asfortranarray(inter_r, dtype='float32'), \
                                               np.asfortranarray(f1, dtype='float32'), \
                                               np.asfortranarray(n, dtype='int32'), \
                                               np.asfortranarray(orb_coeff, dtype='float32'), \
                                               np.asfortranarray(orb_norm_coeff, dtype='float32'), tot_norm, \
                                               np.asfortranarray(tot_zeta, dtype='float32'))
    for i in range(len(kin_1)):
      kin_R.append(0.5*kin_1[i]+6.0*kin_2[i])
  else:
    for i in range(len(dis_R)):
      kin = 0.5*integrate.int_rdRdr_2(dis_R[i], n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta) + \
            6.0*integrate.int_R_2(dis_R[i], n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta)

      kin_R.append(kin)

  return dis_R, kin_R

def find_kin_plateau(kin_R, dis_R, increment, orb):

  kin_R_grad_org = np.gradient(kin_R)
  kin_R_grad = []
  for i in range(len(dis_R)):
    kin_R_grad.append(math.log(10)*dis_R[i]*kin_R_grad_org[i]/increment)
  max_peak_index, _ = signal.find_peaks(kin_R_grad)
  min_peak_index, _ = signal.find_peaks([-x for x in kin_R_grad])
  #kin_grad = kin_R_grad_org[max_peak_index[orb-1]]
  #for i in range(max_peak_index[orb-1], len(kin_R), 1):
  #  if ( abs(kin_R_grad_org[i]) < abs(kin_grad)/50.0 ):
  #    final_index = i
  #    break
  for i in range(max_peak_index[orb-1], len(kin_R), 1):
    if ( abs(kin_R[i]-kin_R[len(kin_R)-1]) < abs(kin_R[len(kin_R)-1])*0.001 ):
      final_index = i
      break

  peak_index = list(min_peak_index[0:(orb-1)])
  peak_index.append(final_index)

  return peak_index
