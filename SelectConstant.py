from Relation import Relation


class SelectConstant(Relation) :
  def __init__(self, attribute_name, constant, subrelation) :
    # check and save subrelation
    if not isinstance(subrelation, Relation) :
      raise TypeError('subrelation argument must be of type Relation"')
    self.subrelation = subrelation
    
    # schema is unchanged
    self.setAttributes(subrelation.getAttributes())
    
    # check are made in getAttribute
    self.attribute = self.getAttribute(attribute_name)
    self.constant = str(constant)
  
  def toSQL(self) :
    comparison = self.attribute.getName()+'="'+self.constant.replace('"', '\\"')+'"'
    return 'SELECT * FROM ('+self.subrelation.toSQL()+') WHERE '+comparison
