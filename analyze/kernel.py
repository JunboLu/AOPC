#! /usr/bin/env python

import os
import csv
import sys
import numpy as np
from AOPC.tools import log_info
from AOPC.tools import data_op
from AOPC.tools import atom_info
from AOPC.analyze import orb_info
from AOPC.analyze import integrate
from AOPC.analyze import kin_ene
from AOPC.analyze import tot_ene
from AOPC.analyze import pot_ene
from AOPC.analyze import screen
from AOPC.analyze import radial_density

log_info.log_logo()

if ( len(sys.argv) != 4 ):
  log_error('Please use AOPC orbital adf_output command', flush=True)
  exit()

orbital = sys.argv[1]
output_file = sys.argv[2]
work_dir = sys.argv[3]

valid_orb = ['1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', \
             '2P', '3P', '4P', '5P', '6P', '7P', '8P', \
             '3D', '4D', '5D', '6D', '7D', \
             '4F', '5F', '6F']

if orbital.upper() not in valid_orb:
  log_info.log_error('The first argv should be orbital, for example, 2p')
  exit()

if not os.path.exists(output_file):
  log_info.log_error('The %s file does not exist' %(output_file))
  exit()

Rmax = 10.0
increment = 0.001
n, orb_coeff, tot_zeta, true_q_num = orb_info.ext_orb(int(orbital[0]), orbital[1].upper(), output_file)
orb_norm_coeff, tot_norm = orb_info.cal_norm(n, orb_coeff, tot_zeta)

atom = orb_info.grep_atom_type(output_file)
orb_ene = orb_info.grep_orb_ene(true_q_num, orbital[1].upper(), output_file)

print ('ORBITAL ENERGY'.center(80, '*'), flush=True)
str_print = 'The orbital energy for %s orbital of %s atom is %f eV\n' %(orbital, atom, orb_ene)
str_print = data_op.str_wrap(str_print, 80)
print (str_print, flush=True)

print ('ORBITAL RADIAL EXPECTATION VALUE'.center(80, '*'), flush=True)

r_exp = integrate.int_r_3_R_2(100, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta)
r2_exp = integrate.int_r_4_R_2(100, n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta)

str_print = 'The expectation value of r for %s orbital of %s atom is %f Bohr' %(orbital, atom, r_exp)
str_print = data_op.str_wrap(str_print, 80)
print (str_print, flush=True)
str_print = 'The expectation value of r2 for %s orbital of %s atom is %f Bohr^2\n' %(orbital, atom, r2_exp)
str_print = data_op.str_wrap(str_print, 80)
print (str_print, flush=True)

print ('RADIAL DENSITY FUNCTION'.center(80, '*'), flush=True)

dis_R, density = radial_density.get_density(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, Rmax, increment)

max_peak_index, min_peak_index = radial_density.find_density_peak(density)

for i in max_peak_index:
  str_print = 'The maximum peak of rdf is in %f Bohr' %(i*increment)
  print (str_print, flush=True)

for i in min_peak_index:
  str_print = 'The node of rdf is in %f Bohr' %(i*increment)
  print (str_print, flush=True)

file_name = ''.join(('density_', atom, '_', orbital, '.csv'))
with open(file_name, 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['R', 'density'])
  for i in range(len(dis_R)):
    writer.writerow([dis_R[i], density[i]])

str_print = 'The radial density function of %s orbital of %s atom is written in %s\n' %(orbital, atom, file_name)
str_print = data_op.str_wrap(str_print, 80)
print (str_print, flush=True)

print ('RADIAL KINETIC ENERGY'.center(80, '*'), flush=True)

if ( orbital[1].upper() == 'S' ):
  dis_R, kin_R = kin_ene.orb_s_kin(n, orb_coeff, orb_norm_coeff, tot_norm, \
                                   tot_zeta, Rmax, increment, output_file, work_dir, atom, orbital)
if ( orbital[1].upper() == 'P' ):
  dis_R, kin_R = kin_ene.orb_p_kin(n, orb_coeff, orb_norm_coeff, tot_norm, \
                                   tot_zeta, Rmax, increment, output_file, work_dir, atom, orbital)
if ( orbital[1].upper() == 'D' ):
  dis_R, kin_R = kin_ene.orb_d_kin(n, orb_coeff, orb_norm_coeff, tot_norm, \
                                   tot_zeta, Rmax, increment, output_file, work_dir, atom, orbital)
if ( orbital[1].upper() == 'F' ):
  dis_R, kin_R = kin_ene.orb_f_kin(n, orb_coeff, orb_norm_coeff, tot_norm, \
                                   tot_zeta, Rmax, increment, output_file, work_dir, atom, orbital)

kin_R_grad = np.gradient(kin_R)
file_name = ''.join(('kin_R_grad_', atom, '_', orbital, '.csv'))
with open(file_name, 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['R', 'kin_R_grad'])
  for i in range(len(dis_R)):
    writer.writerow([dis_R[i], kin_R_grad[i]/increment])

kin_node_index = kin_ene.find_kin_plateau(kin_R, dis_R, increment, true_q_num)
for i in kin_node_index:
  print ('The plateau value of kinetic energy is %f Hartree in %f Bohr' %(kin_R[i], i*increment), flush=True)

file_name = ''.join(('kin_R_', atom, '_', orbital, '.csv'))
with open(file_name, 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['R', 'kinetic'])
  for i in range(len(dis_R)):
    writer.writerow([dis_R[i], kin_R[i]])

str_print = 'The radial kinetic energy of %s orbital of %s atom is written in %s\n' %(orbital, atom, file_name)
str_print = data_op.str_wrap(str_print, 80)
print (str_print, flush=True)

print ('RADIAL TOTAL ENERGY'.center(80, '*'), flush=True)

dis_R, E_tot_R = tot_ene.orb_tot(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, Rmax, increment, orb_ene/27.2107)

file_name = ''.join(('tot_R_', atom, '_', orbital, '.csv'))
with open(file_name, 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['R', 'Total energy'])
  for i in range(len(dis_R)):
    writer.writerow([dis_R[i], E_tot_R[i]])

str_print = 'The radial total energy of %s orbital of %s atom is written in %s\n' %(orbital, atom, file_name)
str_print = data_op.str_wrap(str_print, 80)
print (str_print, flush=True)

print ('RADIAL POTENTIAL ENERGY'.center(80, '*'), flush=True)

pot_R = pot_ene.orb_pot(kin_R, E_tot_R)

pot_R_grad = np.gradient(pot_R)
file_name = ''.join(('pot_R_grad_', atom, '_', orbital, '.csv'))
with open(file_name, 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['R', 'pot_R_grad'])
  for i in range(len(dis_R)):
    writer.writerow([dis_R[i], pot_R_grad[i]/increment])

pot_node_index = pot_ene.find_pot_plateau(pot_R, dis_R, increment, true_q_num)
for i in pot_node_index:
  print ('The plateau value of potential energy is %f Hartree in %f Bohr' %(pot_R[i], i*increment), flush=True)

file_name = ''.join(('pot_R_', atom, '_', orbital, '.csv'))
with open(file_name, 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['R', 'potential'])
  for i in range(len(dis_R)):
    writer.writerow([dis_R[i], pot_R[i]])

str_print = 'The radial potential energy of %s orbital of %s atom is written in %s\n' %(orbital, atom, file_name)
str_print = data_op.str_wrap(str_print, 80)
print (str_print, flush=True)

print ('ATOMIC SCREENING'.center(80, '*'), flush=True)

atom_num = atom_info.get_atom_num(atom)

final_pot_plat = pot_node_index[len(pot_node_index)-1]*increment
screen_R, final_dis_R, final_pot_R = screen.calc_screen(n, orb_coeff, orb_norm_coeff, tot_norm, \
                                     tot_zeta, dis_R, pot_R, final_pot_plat, atom_num)

final_screen = screen.eval_final_screen(density, screen_R, dis_R, final_dis_R)

print ('The screening constant for %s orbital of %s atom is %f' %(orbital, atom, final_screen), flush=True)
print ('The effective charge for %s orbital of %s atom is %f' %(orbital, atom, atom_num-final_screen), flush=True)

file_name = ''.join(('screen_R_', atom, '_', orbital, '.csv'))

with open(file_name, 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['R', 'screen'])
  for i in range(len(screen_R)):
    writer.writerow([final_dis_R[i], screen_R[i]])

str_print = 'The screening constants versus R of %s orbital of %s atom is written in %s' %(orbital, atom, file_name)
str_print = data_op.str_wrap(str_print, 80)
print (str_print, flush=True)

zeff = -(atom_num-final_screen)
pot_R_screen_1 = pot_ene.calc_pot_R_screen(n, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, final_dis_R, screen_R, atom_num)
file_name = ''.join(('pot_screen_R_', atom, '_', orbital, '.csv'))
with open(file_name, 'w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['R', 'potential', 'potential_scr'])
  for i in range(len(final_dis_R)-1):
    writer.writerow([final_dis_R[i], final_pot_R[i], pot_R_screen_1[i]])
