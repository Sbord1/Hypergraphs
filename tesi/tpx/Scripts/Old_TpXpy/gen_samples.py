import os
'A script for generating bitmap or SVG files for all drawings in a specified directory'

tpx_path = 'C:\\WRK\\Delphi\\TpX\\TpX.exe '
pics_path = 'C:\\WRK\\Delphi\\TpX\\Distribution\\Samples\\'
os.chdir(pics_path)
files = os.listdir(pics_path)
for input_filename0 in files:
  if input_filename0.find('.TpX')<0: continue
  input_filename0 = '%s%s'%(pics_path,input_filename0)
#  ext = 'svg'
#  xfrmt = 'latexeps'
  xfrmt = 'latexcustom'
#  xfrmt = 'svg'
  ext = 'qqq'
  code = os.system('%s -f"%s" -x %s -o"%s"'%(tpx_path,input_filename0,xfrmt,input_filename0.replace('.TpX','.'+ext)))
  print input_filename0, code
