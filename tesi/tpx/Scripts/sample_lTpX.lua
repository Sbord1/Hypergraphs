require("lTpX")

pic = TpXpic:Create(
  {PicScale=1, Border=2, TeXFormat="eps", PdfTeXFormat="pdf",
  BitmapRes=11811, PicMagnif=1, IncludePath="",
  LineWidth=0.25, ArrowsSize=0.7, StarsSize=1, MiterLimit=1,
  HatchingStep=1, HatchingLineWidth=0.5, DottedSize=0.5, DashSize=1})
pic:setCaption("A sample TpXpy picture", "fig:TpXpy")
pic:setComment("Comment")
pic:addPolyline({{10,0}, {30,-20}, {15,-30}},
  {fill="mintcream", lw=1.5})
pic:addPolygon({{0,-20}, {10,0}, {15,-30}},
  {fill="floralwhite", lw=1.5})
pic:addLine(0,-20,30,-20, {li="dash"})
pic:addCurve({{0,-10}, {5,-15}, {25,-10}, {15,-5}, {10,-5}},
  {closed=1, lw=0.5, ha=4, hc = "silver"})
pic:addPolygon({{5.56,-8.9}, {12.45,-14.7}, {18.3,-8.3}},
  {li="dot"})
pic:addLine(5.56,-8.9,10,0, {lw=1.5})
pic:addLine(12.45,-14.7,10,0, {lw=1.5})
pic:addLine(18.3,-8.3,10,0, {lw=1.5})
pic:addSector(15, -30, 5.5, 0.6, 1.75, {lw=0.5})
pic:addSector(15, -30, 6.5, 0.6, 1.75, {lw=0.5})
pic:addSector(15, -30, 6, 1.75, 2.55, {lw=0.5})
pic:addCircle(0,-20,0.4, {li="none", fill="navy"})
pic:addCircle(10,0,0.4, {li="none", fill="navy"})
pic:addCircle(15,-30,0.4, {li="none", fill="navy"})
pic:addCircle(30,-20,0.4, {li="none", fill="navy"})
pic:addBitmap(45,-35,65,70, "bg.jpg", {keepaspectratio=0})
pic:addLine(47,0,100,0)
for i = 0, 4 do
  pic:addLine(i*10 + 50,-0.7,i*10 + 50,0.7)
--  pic:addText(i*10 + 50, -1, 3,
  pic:addText(i*10 + 52, -3, 3,
    string.format("%g", i*10), string.format("\\texttt{%g}", i*10),
    {halign="r", rotdeg=45})
end
pic:addLine(100,33,100,-33)
for i = 0, 6 do
  pic:addLine(100-0.7,i*10-30,100+0.7,i*10-30)
  pic:addText(100+6,i*10-30-1, 3,
    string.format("%g", i*10-30),
    string.format("\\texttt{%g}", i*10-30),
    {halign="r"})
end

pp = {}
for i = 0, 49 do
  x = i + 50
  y = 30 * math.sin(x/5.0)
  table.insert(pp, {x, y})
end
pic:addCurve(pp, {li="dot", lw=2})
for i = 0, 49 do
  x = i + 50
  y = 30 * math.sin(x/5.0)
  pic:addStar(x, y + math.sin(i*i*4)*5,
    {s="penta", d=0.8, fill="lightgrey", lw=0.4})
end
d = {0}
dlen = 1
for ll = 1, 8 do
  for i = 1, dlen do table.insert(d, (d[dlen-i+1]+1)%4) end
  dlen = 2*dlen
end
dd0 = {{1,0},{0,1},{-1,0},{0,-1}}
cc = {"blue","goldenrod","green","red"}
step = 2.5
function PP(p)
  local x = p[1]+5
  local y = p[2]+15
  local r = math.sqrt(x*x+y*y)
  local c = 1 - math.cos(r/5)*0.05
  x = x*c
  y = y*c
  x,y = x+0.2*y,y-0.2*x
  return {x/1.5+23, y/1.5+25}
end
for j = 0, 3 do
  pp = {}
  x,y = 0,0
  y = 0
  ddpre = {0, 0}
  p = {0, 0}
  table.insert(pp, PP(p))
  for i = 1, dlen do
    dd = dd0[(d[i]+j)%4+1]
    p = {x-ddpre[1]*step*0.1, y-ddpre[2]*step*0.1}
    table.insert(pp, PP(p))
    p = {x+dd[1]*step*0.1, y+dd[2]*step*0.1}
    table.insert(pp, PP(p))
    p = {x+dd[1]*step*0.5, y+dd[2]*step*0.5}
    table.insert(pp, PP(p))
    x,y = x+dd[1]*step,y+dd[2]*step
    ddpre = dd
  end
  p = {x, y}
  table.insert(pp, PP(p))
  table.insert(pp, PP(p))
  table.insert(pp, PP(p))
  pic:addBezier(pp, {lc=cc[j+1]})
end
pic:addRect(28, -6, 57, 57, {rotdeg=45})
d=2.8
for i = 0, 11 do
  for j = 0, 11 do
    c = HTML_color(
      255*(0.5+0.5*math.sin(i/3.+math.sin(j/3.)*2)),
      255*(0.5+0.5*math.cos(j/3.-i*i/30.)), 0)
    pic:addEllipse(i*d+70,j*d+43,d*0.7,d*0.9,
      {rotdeg=45, fill=c, li="none"})
  end
end
pic:addCurve({{25,75}, {0,65}, {-13,38}},
  {arr1 = "oc", arr2 = "h43", arrs = 0.8, lw=0.5})
pic:addSymbol(52,70,25,"cloud1",
  {lw=0.5, fill="whitesmoke", rotdeg=188})
pic:addText(52,68.5,5,"Fig. 1","", {halign="c"})
fname = "sample_lTpX.TpX"
pic:write(fname)
os.execute(fname)

