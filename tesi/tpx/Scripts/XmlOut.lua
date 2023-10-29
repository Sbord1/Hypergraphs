-- *  Lua module for writing simple XML * --

-- *  Class for writing XML * --

XmlOutput = {}
-- class constructor
function XmlOutput:Create()
  obj = {
    Out = {}, IndentStep = 2, Indent = 0,
    ElStack = {len = 0}, 
    ExpectEOL = false, PreserveSpace = false,
    EOL_Str = "\n"}
  obj.ElStack.Peek = function(self)
    return self[self.len]
  end
  obj.ElStack.Push = function(self, Value)
    local len = self.len + 1
    self.len = len
    self[len] = Value
  end
  obj.ElStack.Pop = function(self)
    local len = self.len
    if len == 0 then error("Element stack is empty") end
    local value = self[len]
    self[len] = nil         -- to allow garbage collection
    self.len = len - 1
    return value
  end
  setmetatable(obj, {__index = self})
  return obj
end
-- write to output stream
function XmlOutput:GetText()
  return table.concat(self.Out)
end
-- write to output stream
function XmlOutput:Write(Data)
  if Data == "" then return end
  table.insert(self.Out, Data)
end
-- a function used internally
function XmlOutput:DataAdded()
  if self.ElStack.len ~= 0 then
    if self.ElStack:Peek().Empty then
      self:Write('>')
      self.ExpectEOL = true
    end
    self.ElStack:Peek().Empty = False
  end
  if self.ExpectEOL then
    if not self.PreserveSpace then self:Write(self.EOL_Str) end
    self.ExpectEOL = false
  end
end
-- open XML tag
function XmlOutput:OpenTag(Tag)
  self:DataAdded()
  Data = {Tag = Tag, Empty = true}
  self.ElStack:Push(Data)
  if not self.PreserveSpace then 
    self:Write(string.rep(" ", self.Indent))
  end
  self:Write("<")
  self:Write(Tag)
  self.Indent = self.Indent + self.IndentStep
end
-- add attribute to current opening tag
function XmlOutput:AddAttribute(Name, Value)
  self:Write(string.format(' %s="%s"', Name, Value))
end
-- add a list of attributes to current opening tag
function XmlOutput:AddAttributes(Attr)
  if Attr then
    for k,v in pairs(Attr) do
      self:Write(string.format(' %s="%s"', k, v))
    end
  end
end
-- add text inside current tag
function XmlOutput:AddText(Data)
  self:DataAdded()
  self:Write(Data)
end
-- close XML tag
function XmlOutput:CloseTag()
  local Data = self.ElStack:Pop()
  self.Indent = self.Indent - self.IndentStep
  if Data.Empty then
    self:Write("/>")
  else
    self:DataAdded()
    if not self.PreserveSpace then 
      self:Write(string.rep(" ", self.Indent))
    end
    self:Write(string.format("</%s>", Data.Tag))
  end
  self.ExpectEOL = true
end
-- add comment to XML
function XmlOutput:AddComment(Data)
  self:DataAdded()
  self:Write(string.format("<!--%s-->", Data))
  self.ExpectEOL = true
end
