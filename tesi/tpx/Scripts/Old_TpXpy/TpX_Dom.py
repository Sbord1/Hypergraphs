import xml.dom.minidom
from TpXpy import TpXpic

def TpX_Dom_as_text(XML):
  t = XML.toprettyxml('  ', '\n')
  t = t.replace('<caption>\n    ','<caption>')
  t = t.replace('\n  </caption>','</caption>')
  t = t.replace('<comment>\n    ','<comment>')
  t = t.replace('\n  </comment>','</comment>')
  t = t.replace('">\n    ','">')
  t = t.replace('\n','\n%')
  j = t.find('\n')
  t = t[j+1:]
  j = t.rfind('\n')
  t = t[:j]
  return t

def TpX_Dom_SaveToFile(XML, FileName):
  f = file(FileName, 'w')
  f.write(TpX_Dom_as_text(XML))
  f.close()

def TpX_Dom_LoadFromFile(FileName):
  lines = file(FileName, 'r').readlines()
  for i in range(0,len(lines)):
    if lines[i][:1]=='%':
      lines[i] = lines[i][1:].strip()
    else: break
  return xml.dom.minidom.parseString(''.join(lines))

dom = TpX_Dom_LoadFromFile('sample_TpXpy.TpX')
nodes = dom.documentElement.childNodes
for node in nodes:
  if node.nodeType == node.ELEMENT_NODE:
    if node.getAttribute('lw')=='1.5':
      node.setAttribute('lw', '3')
    if node.getAttribute('li')=='':
      node.setAttribute('fill', 'green')
    #node.setAttribute('q', 'value')
TpX_Dom_SaveToFile(dom, 'sample_TpXpy_3.TpX')
dom.unlink()