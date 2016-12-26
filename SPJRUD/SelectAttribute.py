from Relation import Relation
from functions import *


# Operator Select to access an attribute (or column)
class SelectAttribute(Relation) :
  def __init__(self, attribute_name_1, attribute_name_2, subrelation) :
    # check and save subrelation
    self.subrelation = check_relation(self, subrelation, 'subrelation')
    
    # schema is unchanged
    self.setAttributes(subrelation.getAttributes())
    
    # checks are made in getAttribute
    self.attribute1 = self.getAttribute(attribute_name_1, True, 'subrelation')
    self.attribute2 = self.getAttribute(attribute_name_2, True, 'subrelation')
    
    # check that attribute1 and attribute2 are comparable
    if not self.attribute1.isComparableTo(self.attribute2) :
      self.error(str(self.attribute1)+' is not comparable with '+str(self.attribute2))
  
  def toSQL(self) :
    comparison = '"'+self.attribute1.getName()+'"="'+self.attribute2.getName()+'"'
    # query
    return 'SELECT * FROM ('+self.subrelation.toSQL()+') WHERE '+comparison
