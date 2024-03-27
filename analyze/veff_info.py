#! /usr/bin/env python

import linecache
import numpy as np
from scipy.interpolate import interp1d
from AOPC.tools import data_op
from AOPC.tools import call
from AOPC.tools import log_info

def get_veff(work_dir, file_name, atom, orb):

  dmp_exe = call.call_returns_shell(work_dir, 'which dmpkf')
  if ( len(dmp_exe) == 0 or 'no dmpkf in' in dmp_exe[0] ):
    log_info.log_error('Envrionment error: can not find dmpkf executable file, please set the environment for adf')
    exit()

  out_file = ''.join(('veff', '_', atom, '_', orb))
  cmd = "dmpkf %s 'Atyp  1 %s%%core totpot ext' > %s" %(file_name, atom, out_file)
  call.call_simple_shell(work_dir, cmd)
  whole_line_num_1 = len(open(out_file).readlines())

  veff = []
  for i in range(whole_line_num_1-3):
    line = linecache.getline(out_file, i+4)
    line_split = data_op.split_str(line, ' ', '\n')
    for j in range(len(line_split)):
      veff.append(float(line_split[j]))

  cmd = 'rm %s' %(out_file)
  call.call_simple_shell(work_dir, cmd)

  return veff 

def get_rmin(work_dir, file_name, atom, orb):

  out_file = ''.join(('rmin', '_', atom, '_', orb))
  cmd = "dmpkf %s 'Atyp  1 %s%%rmin' > %s" %(file_name, atom, out_file)
  call.call_simple_shell(work_dir, cmd)

  line = linecache.getline(out_file, 4)
  line_split = data_op.split_str(line, ' ', '\n')

  rmin = float(line_split[0])

  cmd = 'rm %s' %(out_file)
  call.call_simple_shell(work_dir, cmd)

  return rmin

def get_rfac(work_dir, file_name, atom, orb):

  out_file = ''.join(('rfac', '_', atom, '_', orb))
  cmd = "dmpkf %s 'Atyp  1 %s%%rfac' > %s" %(file_name, atom, out_file)
  call.call_simple_shell(work_dir, cmd)

  line = linecache.getline(out_file, 4)
  line_split = data_op.split_str(line, ' ', '\n')

  rfac = float(line_split[0])

  cmd = 'rm %s' %(out_file)
  call.call_simple_shell(work_dir, cmd)

  return rfac

def kernel(work_dir, file_name, atom, orb):

  veff = get_veff(work_dir, file_name, atom, orb)
  rmin = get_rmin(work_dir, file_name, atom, orb)
  rfac = get_rfac(work_dir, file_name, atom, orb)

  r = []
  for i in range(len(veff)):
    r.append(rmin*rfac**(i))

  inter_r = np.arange(0.000002, 10.000001, 0.000001)
  interp_func = interp1d(r, veff, kind='cubic')

  inter_veff = interp_func(list(inter_r))

  f1 = []
  for i in range(len(inter_r)):
    f1.append(1.0/(1.0-inter_veff[i]/(2*137.03599976**2)))

  return inter_r, f1
