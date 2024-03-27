#! /usr/bin/env python

import numpy as np

def fast_exponentiation(base, exponent):

  result = 1
  while exponent > 0:
      if exponent % 2 == 1:
          result *= base
      base *= base
      exponent //= 2
  return result

def int_gamma_0(zeta, R):

  R = zeta*R
  return zeta**(-1)*(-np.exp(-R))

def int_gamma_1(zeta, R):

  R = zeta*R
  return zeta**(-2)*(-(R+1)*np.exp(-R))

def int_gamma_2(zeta, R):

  R = zeta*R
  return zeta**(-3)*(-(R**2+2*R+2)*np.exp(-R))

def int_gamma_3(zeta, R):

  R = zeta*R
  return zeta**(-4)*(-(R**3+3*R**2+6*R+6)*np.exp(-R))

def int_gamma_4(zeta, R):

  R = zeta*R
  return zeta**(-5)*(-(R**4+4*R**3+12*R**2+24*R+24)*np.exp(-R))

def int_gamma_5(zeta, R):

  R = zeta*R
  return zeta**(-6)*(-(R**5+5*R**4+20*R**3+60*R**2+120*R+120)*np.exp(-R))

def int_gamma_6(zeta, R):

  R = zeta*R
  return zeta**(-7)*(-(R**6+6*R**5+30*R**4+120*R**3+360*R**2+720*R+720)*np.exp(-R))

def int_gamma_7(zeta, R):

  R = zeta*R
  return zeta**(-8)*(-(R**7+7*R**6+42*R**5+210*R**4+840*R**3+2520*R**2+5040*R+5040)*np.exp(-R))

def int_gamma_8(zeta, R):

  R = zeta*R
  return zeta**(-9)*(-(R**8+8*R**7+56*R**6+336*R**5+1680*R**4+6720*R**3+20160*R**2+40320*R+40320)*np.exp(-R))

def int_gamma_9(zeta, R):

  R = zeta*R
  return zeta**(-10)*(-(R**9+9*R**8+72*R**7+504*R**6+3024*R**5+15120*R**4+\
         60480*R**3+181440*R**2+362880*R+362880)*np.exp(-R)+362880)

def int_gamma_10(zeta, R):

  R = zeta*R
  return zeta**(-11)*(-(R**10+10*R**9+90*R**8+720*R**7+5040*R**6+30240*R**5+151200*R**4+\
         604800*R**3+1814400*R**2+3628800*R+3628800)*np.exp(-R))

def int_gamma_11(zeta, R):

  R = zeta*R
  return zeta**(-12)*(-(R**11+11*R**10+110*R**9+990*R**8+7920*R**7+55440*R**6+332640*R**5+\
         1663200*R**4+6652800*R**3+19958400*R**2+39916800*R+39916800)*np.exp(-R))

def int_gamma_12(zeta, R):

  R = zeta*R
  return zeta**(-13)*(-(R**12+12*R**11+132*R**10+1320*R**9+11880*R**8+95040*R**7+665280*R**6+\
         3991680*R**5+19958400*R**4+79833600*R**3+239500800*R**2+479001600*R+479001600)*np.exp(-R))

def int_gamma_13(zeta, R):

  R = zeta*R
  return zeta**(-14)*(-(R**13+13*R**12+156*R**11+1716*R**10+17160*R**9+154440*R**8+1235520*R**7+8648640*R**6+\
         51891840*R**5+259459200*R**4+1037836800*R**3+3113510400*R**2+6227020800*R+6227020800)*np.exp(-R))

def int_gamma_14(zeta, R):

  R = zeta*R
  return zeta**(-15)*(-(R**14+14*R**13+182*R**12+2184*R**11+24024*R**10+240240*R**9+\
         2162160*R**8+17297280*R**7+121080960*R**6+726485760*R**5+3632428800*R**4+\
         14529715200*R**3+43589145600*R**2+87178291200*R+87178291200)*np.exp(-R))

def int_gamma_15(zeta, R):

  R = zeta*R
  return zeta**(-16)*(-(R**15+15*R**14+210*R**13+2730*R**12+32760*R**11+360360*R**10+\
         3603600*R**9+32432400*R**8+259459200*R**7+1816214400*R**6+10897286400*R**5+\
         54486432000*R**4+217945728000*R**3+653837184000*R**2+1307674368000*R+1307674368000)*np.exp(-R))

def int_gamma_16(zeta, R):

  R = zeta*R
  return zeta**(-17)*(-(R**16+16*R**15+240*R**14+3360*R**13+43680*R**12+524160*R**11+5765760*R**10+\
         57657600*R**9+518918400*R**8+4151347200*R**7+29059430400*R**6+174356582400*R**5+\
         871782912000*R**4+3487131648000*R**3+10461394944000*R**2+20922789888000*R+20922789888000)*np.exp(-R))


