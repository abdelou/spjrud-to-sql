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
    self.attributes = []
    for attr in subrelation.getAttributes() :
      if attr.getName() in only_attributes :
        self.attributes.append(attr)
    
  def toSQL(self) :
    att = ','.join(self.getAttributesName())
    return 'SELECT '+att+' FROM ('+self.subrelation.toSQL()+')'
