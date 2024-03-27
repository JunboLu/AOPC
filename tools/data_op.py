#! /usr/bin/env python

from AOPC.tools import call

def str_wrap(str_tmp, max_width, indent_char=''):

  if ( len(str_tmp) <= max_width ):
    return indent_char+str_tmp
  else:
    max_width = max_width - len(indent_char)
    list_tmp = [str_tmp[i:i+max_width] for i in range(0, len(str_tmp), max_width)]
    for i in range(len(list_tmp)):
      list_tmp[i] = indent_char + list_tmp[i]
    str_wrap = '\n'.join(list_tmp)
    return str_wrap

def split_str(str_tmp, space_char, strip_char=''):


  str_tmp_split = str_tmp.split(space_char)
  list_tmp = []
  for i in range(len(str_tmp_split)):
    if ( str_tmp_split[i] != ''):
      list_tmp.append(str_tmp_split[i])

  if ( strip_char != '' ):
    if ( list_tmp[len(list_tmp)-1] == strip_char ):
      list_tmp.remove(list_tmp[len(list_tmp)-1])
    else:
      list_tmp[len(list_tmp)-1] = list_tmp[len(list_tmp)-1].strip(strip_char)

  return list_tmp

def grep_line_num(choosed_str, file_name, work_dir):

  line_num = []
  cmd = 'grep -n "%s" %s' %(choosed_str, file_name)
  line = call.call_returns_shell(work_dir, cmd)
  if ( len(line) >= 1 and 'Binary file' in line[0] ):
    cmd = 'grep -a -n "%s" %s' %(choosed_str, file_name)
    line = call_returns_shell(work_dir, cmd)
  if ( len(line) != 0 ):
    for i in range(len(line)):
      line_num.append(int(line[i].split(':')[0]))
  else:
    line_num = 0

  return line_num


