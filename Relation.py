from pprint import pprint

class Relation :
  def __init__(self, attributes) :
    self.setAttributes(attributes)
  
  def setAttributes(self, attributes) :
    if not isinstance(attributes, list) :
      raise TypeError('attributes argument must be a list of objects Attribute"')
    
    for attr in attributes :
      if not isinstance(attr, Attribute) :
        raise TypeError('Attribute "'+attr+'" is not of type Attribute')
    
    self.attributes = attributes
  
  def getAttribute(self, attribute_name) :
    for attr in self.attributes :
      if attr.getName() == attribute_name :
        return attr
    raise Exception('Relation has no attribute named "'+attribute_name+'"')
  
  def getAttributes(self) :
    return self.attributes
  
  def getAttributesName(self) :
    names = []
    for attr in self.attributes :
      names.append(attr.getName())
    return names
  
  def toSQL(self) :
    raise Exception('method toSQL not implemented here')

class Attribute :
  # datatypes from https://www.sqlite.org/datatype3.html and FLOAT return by PRAGMA TABLE_INFO()
  valid_types = ['TEXT', 'NUMERIC', 'INTEGER', 'REAL', 'BLOB', 'FLOAT']
  def __init__(self, name, type) :
    # TODO : check name ?
    self.name = name
    # check type
    if not type in Attribute.valid_types :
      raise TypeError('Invalid type "'+type+'" for attribute "'+name+'"')
    self.type = type
  
  def isComparableTo(self, other) :
    if not isinstance(other, Attribute) :
      return False
    # numeric can be compared with numeric so only text cannot be compared with other
    if self.getType() == 'TEXT' and other.getType() != 'TEXT' :
      return False
    if other.getType() == 'TEXT' and self.getType() != 'TEXT' :
      return False
    return True
  
  def getName(self) :
    return self.name
  
  def getType(self) :
    return self.type
  
  def __str__(self) :
    return 'Attribute "'+self.getName()+'" of type "'+self.getType()+'"'


