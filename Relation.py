from pprint import pprint


# 'Abstract' class used as a base for all Operators. Made of a list of objects of type Attribute
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
        raise TypeError('Attribute "'+str(attr)+'" is not of type Attribute')
    
    self.attributes = attributes
  
  # return Attribute of name attribute_name
  def getAttribute(self, attribute_name, raise_error=True, rel_name='Relation') :
    for attr in self.attributes :
      if attr.getName() == attribute_name :
        return attr
    if raise_error :
      self.error(rel_name+' has no attribute named "'+attribute_name+'"')
    return False
  
  # return list of Attributes
  def getAttributes(self) :
    return self.attributes
  
  # return name of all Attributes
  def getAttributesName(self) :
    names = []
    for attr in self.attributes :
      names.append(attr.getName())
    return names
  
  # abstract method to be defined in each subclass
  def toSQL(self) :
    self.error('method toSQL not implemented here')
  
  # raises an error with an info about the subclass name
  def error(self, message) :
    raise Exception(self.__class__.__name__+' : '+message)

# class used to represent each column (attribute) in a table (relation).
class Attribute :
  # see README for more informations about data types
  valid_types = ['TEXT', 'NUMERIC', 'INTEGER', 'REAL', 'BLOB', 'FLOAT']
  
  # construct object with a string name and a type from valid_types
  def __init__(self, name, type) :
    self.setName(name)
    self.setType(type)
  
  def isComparableTo(self, other) :
    if not isinstance(other, Attribute) :
      return False
    # see README for more informations about data comparison
    if self.getType() == 'TEXT' and other.getType() != 'TEXT' :
      return False
    if other.getType() == 'TEXT' and self.getType() != 'TEXT' :
      return False
    return True
  
  # some more checks could be done but names are excaped within requests
  def setName(self, name) :
    self.name = unicode(name)
  
  def getName(self) :
    return self.name
  
  # check type, see README for more informations about data types
  def setType(self, type) :
    if not type in Attribute.valid_types :
      raise TypeError('Invalid type "'+type+'"')
    self.type = type
  
  def getType(self) :
    return self.type
  
  def __str__(self) :
    return 'Attribute "'+self.getName()+'" of type "'+self.getType()+'"'


