from Relation import Relation
from functions import *
from copy import deepcopy


class Join(Relation) :
  def __init__(self, subrelation1, subrelation2) :
    # check and save subrelations
    self.subrelation1 = check_relation(self, subrelation1, 'subrelation1')
    self.subrelation2 = check_relation(self, subrelation2, 'subrelation2')
    
    # copy at least attributes from attributes1
    attributes = deepcopy(subrelation1.getAttributes())
    
    # check if all attributes are the same, it is an intersection (not managed by SQL JOIN)
    if attributes_match(subrelation1.getAttributes(), subrelation2.getAttributes()) :
      self.intersect = True
      self.setAttributes(attributes)
      return
    else :
      self.intersect = False
    
    # check that common attributes have same type and add uncommon ones
    for attr2 in subrelation2.getAttributes() :
      attr1 = subrelation1.getAttribute(attr2.getName(), False)
      # add uncommon attributes
      if not attr1 :
        attributes.append(attr2)
      # common attribute with different types
      elif attr1.getType() != attr2.getType() :
        self.error(str(attr1)+' in subrelation1 is not the same type as '+str(attr2)+' in subrelation2')
    
    self.setAttributes(attributes)
    
  def toSQL(self) :
    if self.intersect :
      return 'SELECT * FROM ('+self.subrelation1.toSQL()+') INTERSECT SELECT * FROM ('+self.subrelation2.toSQL()+')'
    # NATURAL JOIN is equivalent to JOIN USING [COMMON_ATTRIBUTES]
    return 'SELECT * FROM ('+self.subrelation1.toSQL()+') NATURAL JOIN ('+self.subrelation2.toSQL()+')'
