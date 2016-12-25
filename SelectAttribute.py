from Relation import Relation


class SelectAttribute(Relation) :
  def __init__(self, attribute_name_1, attribute_name_2, subrelation) :
    # check and save subrelation
    if not isinstance(subrelation, Relation) :
      raise TypeError('subrelation argument must be of type "Relation"')
    self.subrelation = subrelation
    
    # schema is unchanged
    self.setAttributes(subrelation.getAttributes())
    
    # check are made in getAttribute
    self.attribute1 = self.getAttribute(attribute_name_1)
    self.attribute2 = self.getAttribute(attribute_name_2)
    
    if not self.attribute1.isComparableTo(self.attribute2) :
      raise Exception(str(self.attribute1)+' is not comparable with '+str(self.attribute2))
  
  def toSQL(self) :
    comparison = '"'+self.attribute1.getName()+'"="'+self.attribute2.getName()+'"'
    return 'SELECT * FROM ('+self.subrelation.toSQL()+') WHERE '+comparison
