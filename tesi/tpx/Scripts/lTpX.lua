-- *  Lua module for writing TpX files * --

require("XmlOut")

-- *  Class for creating TpX drawing * --

TpXpic = {} -- a table holding the class methods
-- constructor
function TpXpic:Create(Attr)
  obj = {XmlOut = XmlOutput:Create(), Opened = true}
  obj.XmlOut.EOL_Str = "\n\%"
  obj.XmlOut:Write("\%")
  obj.XmlOut:OpenTag("TpX")
  obj.XmlOut:AddAttribute("v", "5")
  obj.XmlOut:AddAttributes(Attr) 
  setmetatable(obj, {__index = self})
   -- class methods are searched in TpXpic table
  return obj
end
-- finish and write to file
function TpXpic:write(Filename)
  if self.Opened then
    self.XmlOut:CloseTag()
    self.Opened = false
  end
  if Filename ~= nil then
    io.output(Filename)
    io.write(self.XmlOut:GetText())
    io.close()
  else
    print(self.XmlOut:GetText())
  end
end
-- set caption and/or label
function TpXpic:setCaption(s, label)
  self.XmlOut:OpenTag("caption")
  if label then self.XmlOut:AddAttribute("label", label) end
  self.XmlOut:AddText(s)
  self.XmlOut:CloseTag()
end
-- set comment
function TpXpic:setComment(s)
  self.XmlOut:OpenTag("comment")
  self.XmlOut.PreserveSpace = true
  self.XmlOut:AddText(s)
  self.XmlOut:CloseTag()
  self.XmlOut.PreserveSpace = false
end
-- Common attributes
-- lc = set line color
-- lw = set line width
-- li = set line style: none, dot, dash or solid (default)
-- ha = set hatching: 1,...,6
-- hc = set hatching color
-- fill = set fill color
-- arr1 =
-- arr2 = add arrow-head:
--       none, h40, h41, h42, h43, h44, h45, h46, h47, h48,
--       t40, t43, t44, t45, h20, h21, h22, h23, h24,
--       t20, t21, t22, t23, hr10, hr11, hr12, tr10,
--       h10, h11, h12, h12c, t10, r0, r10, r11, r12,
--       r20, r20c, r21, r33, ts10, ts11, ts12, hs10, hs12,
--       ts20, ts21, ts23, hs20, hs23, o, oc, qq;"
-- arrs = set arrow-head size factor
-- rotdeg = set rotation angle
-- closed = make a curve closed: 1
-- halign = set text horizontal alignment:
--       l (left, default), c (center) or r (right)
-- s = set star shape:
--       circle (default), square, diamond, triup, tridown, penta,
--       star4, star5, star6, cross, dcross, flower5, flower4,
--       star4arc, maltese
-- d = set star size factor
-- keepaspectratio = keep bitmap aspect ratio
--  (0: do not keep, 1: default)
--
-- add line
function TpXpic:addLine(x1, y1, x2, y2, Attr)
  self.XmlOut:OpenTag("line")
  self.XmlOut:AddAttributes(
    {x1 = x1, y1 = y1, x2 = x2, y2 = y2})
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end
-- add rectangle
function TpXpic:addRect(x, y, w, h, Attr)
  self.XmlOut:OpenTag("rect")
  self.XmlOut:AddAttributes(
    {x = x, y = y, w = w, h = h})
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end
-- add circle
function TpXpic:addCircle(x, y, d, Attr)
  self.XmlOut:OpenTag("circle")
  self.XmlOut:AddAttributes(
    {x = x, y = y, d = d})
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end
-- add ellipse
function TpXpic:addEllipse(x, y, dx, dy, Attr)
  self.XmlOut:OpenTag("ellipse")
  self.XmlOut:AddAttributes(
    {x = x, y = y, dx = dx, dy = dy})
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end
-- add an object with points
function TpXpic:addPoints(Tag, pp, Attr)
  self.XmlOut:OpenTag(Tag)
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut.PreserveSpace = true
  local tmpList = {}
  for _,v in ipairs(pp) do
    table.insert(tmpList, string.format("%g,%g", v[1], v[2]))
  end
  self.XmlOut:AddText(table.concat(tmpList, " "))
  self.XmlOut:CloseTag()
  self.XmlOut.PreserveSpace = false
end
-- add polyline
function TpXpic:addPolyline(pp, Attr)
  self:addPoints("polyline", pp, Attr)
end
-- add polygon
function TpXpic:addPolygon(pp, Attr)
  self:addPoints("polygon", pp, Attr)
end
-- add circular primitive
function TpXpic:addCircular(Tag, x, y, d, a1, a2, Attr)
  self.XmlOut:OpenTag(Tag)
  self.XmlOut:AddAttributes(
    {x = x, y = y, d = d, a1 = a1, a2 = a2})
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end
-- add arc
function TpXpic:addArc(x, y, d, a1, a2, Attr)
  self:addCircular('arc', x, y, d, a1, a2, Attr)
end
-- add segment
function TpXpic:addSegment(x, y, d, a1, a2, Attr)
  self:addCircular('segment', x, y, d, a1, a2, Attr)
end
-- add sector
function TpXpic:addSector(x, y, d, a1, a2, Attr)
  self:addCircular('sector', x, y, d, a1, a2, Attr)
end
-- add curve
function TpXpic:addCurve(pp, Attr)
  self:addPoints("curve", pp, Attr)
end
-- add Bezier path
function TpXpic:addBezier(pp, Attr)
  self:addPoints("bezier", pp, Attr)
end
-- add text label
function TpXpic:addText(x, y, h, t, tex, Attr)
  self.XmlOut:OpenTag("text")
  self.XmlOut:AddAttributes(
    {x = x, y = y, h = h, t = t, a2 = a2})
  self.XmlOut:AddAttribute("tex", tex) 
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end
-- add star
function TpXpic:addStar(x, y, Attr)
  self.XmlOut:OpenTag("star")
  self.XmlOut:AddAttributes(
    {x = x, y = y})
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end
-- add symbol
-- s = set symbol shape:
--       process, decision, input-output, preparation, punch-card,
--       manual-op, keyboard, punch-tape, document, documents,
--       display, terminal, keying, alt-process, online-storage,
--       magnetic-drum, magnetic-tape, hoarrow1, hoarrow1v,
--       hoarrow2, hoarrow3, hoarrow4, star5, diamond8, baloon1,
--       baloon2, cloud1, splash1, snowflake1
function TpXpic:addSymbol(x, y, d, s, Attr)
  self.XmlOut:OpenTag("symbol")
  self.XmlOut:AddAttributes(
    {x = x, y = y, d = d, s = s})
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end
-- add bitmap
function TpXpic:addBitmap(x, y, w, h, link, Attr)
  self.XmlOut:OpenTag("bitmap")
  self.XmlOut:AddAttributes(
    {x = x, y = y, w = w, h = h, link = link})
  self.XmlOut:AddAttributes(Attr)
  self.XmlOut:CloseTag()
end

-- *  Make HTML color from RGB levels * --

function round(x)
  return math.floor(x+0.5)
end

function HTML_color(r,g,b) 
  r = round(r)
  if r<0 then r=0 end
  if r>255 then r=255 end
  g = round(g)
  if g<0 then g=0 end
  if g>255 then g=255 end
  b = round(b)
  if b<0 then b=0 end
  if b>255 then b=255 end
  return string.format("#%02X%02X%02X", r, g, b)
end

