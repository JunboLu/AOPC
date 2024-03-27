#! /usr/bin/env python

import subprocess
from AOPC.tools import log_info
from subprocess import check_call, Popen, STDOUT, CalledProcessError

def call_simple_shell(exe_dir, cmd):

  #check_call is better. We could use call, check_call and run here.
  #But we need higher version python if we use run.
  try:
    check_call(cmd, cwd=exe_dir, shell=True)
  except CalledProcessError as err:
    log_info.log_error('Running error: %s command running error in %s' %(err.cmd, exe_dir))

def call_returns_shell(exe_dir, cmd):

  p = Popen(cmd, cwd=exe_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  (stdoutput, erroutput) = p.communicate()
  stdoutput = stdoutput.decode()
  output = stdoutput.split('\n')
  output.remove('')

  return output

