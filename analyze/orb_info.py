#! /usr/bin/env python

import math
import linecache
import numpy as np
from AOPC.tools import data_op

def ext_orb(q_num, orb_type, output_file):

  line_1_num = data_op.grep_line_num('Valence Basis Sets:', output_file, './')[0]
  if ( orb_type == 'S' ):
    line_2_num = data_op.grep_line_num('=== S ===', output_file, './')[1]
    q_num = q_num-0
  elif ( orb_type == 'P' ):
    line_2_num = data_op.grep_line_num('=== P:y ===', output_file, './')[1]
    q_num = q_num-1
  elif ( orb_type == 'D' ):
    line_2_num = data_op.grep_line_num('=== D:xz ===', output_file, './')[1]
    q_num = q_num-2
  elif ( orb_type == 'F' ):
    line_2_num = data_op.grep_line_num('=== F:xyz ===', output_file, './')[1]
    q_num = q_num-3
  else:
    print ('%s orbital does not support!', flush=True)
    exit()

  n = []
  tot_zeta = []
  orb_coeff = []

  whole_line_num_1 = len(open(output_file).readlines())

  for i in range(whole_line_num_1-line_1_num):
    line = linecache.getline(output_file, i+line_1_num+2)
    line_split = data_op.split_str(line, ' ', '\n')
    if ( len(line_split) != 0 ):
      if ( line_split[1] == orb_type ):
        n.append(int(line_split[0]))
        tot_zeta.append(float(line_split[len(line_split)-1]))
    else:
      break
  for i in range(len(n)):
    if ( q_num%4 == 0 ):
      col = 4
      block = int(q_num/4)-1
    else:
      col = q_num%4
      block = int(q_num/4)
    line = linecache.getline(output_file, i+1+line_2_num+block*(len(n)+3)+6)
    line_split = data_op.split_str(line, ' ', '\n')
    orb_coeff.append(float(line_split[col]))

  return n, orb_coeff, tot_zeta, q_num

def cal_norm(n, orb_coeff, tot_zeta):

  orb_norm_coeff = []
  for i in range(len(orb_coeff)):
    orb_norm_coeff.append((2*tot_zeta[i])**(n[i]+0.5)/np.sqrt(math.factorial(2*n[i])))

  sum_value = 0.0
  for i in range(len(orb_coeff)):
    for j in range(len(orb_coeff)):
      sum_value = sum_value+np.math.factorial(n[i]+n[j])/(tot_zeta[i]+tot_zeta[j])**(n[i]+n[j]+1)*\
                  orb_coeff[i]*orb_norm_coeff[i]*orb_coeff[j]*orb_norm_coeff[j]

  tot_norm = np.sqrt(sum_value)

  return orb_norm_coeff, tot_norm

def grep_orb_ene(q_num, orb_type, output_file):

  phrase = ''.join(('%     ', str(q_num), ' ', orb_type))
  line_num = data_op.grep_line_num(phrase, output_file, './')[0]
  line = linecache.getline(output_file, line_num)
  line_split = data_op.split_str(line, ' ', '\n')
  if ( len(line_split) < 8 ):
    line_num = data_op.grep_line_num(phrase, output_file, './')[1]
    line = linecache.getline(output_file, line_num)
    line_split = split_str(line, ' ', '\n')

  return float(line_split[0])

def grep_atom_type(output_file):

  line_num = data_op.grep_line_num('atom        charge', output_file, './')[0]
  line = linecache.getline(output_file, line_num+2)
  line_split = data_op.split_str(line, ' ', '\n')

  return line_split[1]


