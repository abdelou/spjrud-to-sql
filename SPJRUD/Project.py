from Relation import Relation
from Functions import *


class Project(Relation) :
  def __init__(self, only_attributes, subrelation) :
    # check that argument subrelation is an object of type Relation
    check_relation(subrelation, 2)
    self.subrelation = subrelation
    
    # check that attributes are in subAttributes
    subAttributesName = subrelation.getAttributesName()
    for attr in only_attributes :
      if not attr in subAttributesName :
        raise Exception('Sub-Relation of Project has no attribute "'+attr+'"')
        
    # create new schema with only only_attributes
    attributes = []
    for attr in subrelation.getAttributes() :
      if attr.getName() in only_attributes :
        attributes.append(attr)
    self.setAttributes(attributes)
    
  def toSQL(self) :
    # join and escape attributes' names because they can contain spaces
    columns = '"'+'","'.join(self.getAttributesName())+'"'
    # query
    return 'SELECT '+columns+' FROM ('+self.subrelation.toSQL()+')'
