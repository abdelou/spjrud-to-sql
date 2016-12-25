from Relation import Relation


class Project(Relation) :
  def __init__(self, only_attributes, subrelation) :
    if not isinstance(subrelation, Relation) :
      raise TypeError('subrelation argument must be of type Relation"')
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
    # join and escape attributes name because they can contain spaces
    columns = '"'+'","'.join(self.getAttributesName())+'"'
    return 'SELECT '+columns+' FROM ('+self.subrelation.toSQL()+')'
