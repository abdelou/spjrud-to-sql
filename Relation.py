from pprint import pprint


# 'Abstract' class used as a base for all Operators. Made of a list of objects of type Attributes
class Relation :
  def __init__(self, attributes) :
    self.setAttributes(attributes)
  
  def setAttributes(self, attributes) :
    # check that the entry arguments is an object of type List
    if not isinstance(attributes, list) :
      raise TypeError('attributes argument must be a list of objects Attribute"')
    
    # check that all objects in the list are of type Attribute
    for attr in attributes :
      if not isinstance(attr, Attribute) :
        raise TypeError('Attribute "'+attr+'" is not of type Attribute')
    
    self.attributes = attributes
  
  # return Attribute of name attribute_name
  def getAttribute(self, attribute_name, raise_error=True) :
    for attr in self.attributes :
      if attr.getName() == attribute_name :
        return attr
    if not raise_error :
      return False
    raise Exception('Relation has no attribute named "'+attribute_name+'"')
  
  # return list of Attributes
  def getAttributes(self) :
    return self.attributes
  
  # return name of all Attributes
  def getAttributesName(self) :
    names = []
    for attr in self.attributes :
      names.append(attr.getName())
    return names
  
  def toSQL(self) :
    raise Exception('method toSQL not implemented here')

# class used to represent each column (attribute) in a table (relation).
class Attribute :
  # datatypes from https://www.sqlite.org/datatype3.html and FLOAT return by PRAGMA TABLE_INFO()
  valid_types = ['TEXT', 'NUMERIC', 'INTEGER', 'REAL', 'BLOB', 'FLOAT']
  def __init__(self, name, type) :
    self.setName(name)
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
  
  def setName(self, name) :
    # TODO : check name ?
    self.name = unicode(name)
  
  def getName(self) :
    return self.name
  
  def getType(self) :
    return self.type
  
  def __str__(self) :
    return 'Attribute "'+self.getName()+'" of type "'+self.getType()+'"'


