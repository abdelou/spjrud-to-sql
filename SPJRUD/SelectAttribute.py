from Relation import Relation
from Functions import *


# Operator Select to access an attribute (or column)
class SelectAttribute(Relation) :
  def __init__(self, attribute_name_1, attribute_name_2, subrelation) :
    # check and save subrelation
    check_relation(subrelation, 3)
    self.subrelation = subrelation
    
    # schema is unchanged
    self.setAttributes(subrelation.getAttributes())
    
    # checks are made in getAttribute
    self.attribute1 = self.getAttribute(attribute_name_1)
    self.attribute2 = self.getAttribute(attribute_name_2)
    
    # check that attribute1 and attribute2 are comparable
    if not self.attribute1.isComparableTo(self.attribute2) :
      raise Exception(str(self.attribute1)+' is not comparable with '+str(self.attribute2))
  
  def toSQL(self) :
    comparison = '"'+self.attribute1.getName()+'"="'+self.attribute2.getName()+'"'
    # query
    return 'SELECT * FROM ('+self.subrelation.toSQL()+') WHERE '+comparison
