# AOPC - A program to calculate atomic properties
---------

The code is mainly written in Python and Fortran.  

Email: lujunbo15@gmail.com
  
# Installation for DPFlow

* Prerequisites
   - Python 3.5 or higher
   - Numpy 1.8.0 or higher

* Compile core module
  
    cd AOPC_directory/lib  
    f2py3.10 -c fast_int_mod.f90 -m fast_int_mod 
    !Caution: If your gcc version is low, f2py cannot compile core code please  
    update your gcc up to 6.3.  

* Environmental variable

    export PYTHONPATH=../AOPC_directory:$PYTHONPATH  
    change python_exe and AOPC directory in AOPC_directory/bin/AOPC file  
    export PATH=AOPC_directory/bin:$PATH  

# How to use 
* AOPC is an user-friendly code.  

  AOPC uses the result calculated by ADF.  
  Users just need to run:  
  AOPC 7s U.out  
