-- A Lua script for refreshing all drawings in a specified directory

require "lfs" -- depends on LuaFileSystem library!

tpx_path = '................/TpX.exe '
pics_path = '................/'
files = lfs.dir(pics_path)
for input_filename0 in files do
  -- Skip non-TpX files
  if string.sub(input_filename0, -4, -1) == '.TpX' then
    input_filename0 = pics_path .. input_filename0
    code = os.execute(string.format(
      '%s -f"%s" -o', tpx_path, input_filename0))
    print(input_filename0, code)
  end
end
