from Relation import Relation
from functions import *
from copy import deepcopy


class Join(Relation) :
  def __init__(self, subrelation1, subrelation2) :
    # check and save subrelations
    self.subrelation1 = check_relation(self, subrelation1, 'subrelation1')
    self.subrelation2 = check_relation(self, subrelation2, 'subrelation2')
    
    # copy at least attributes from attributes1
    self.setAttributes(deepcopy(subrelation1.getAttributes()))
    # make list of common attributes for future use
    self.common_attributes_name = []
    
    # check if all attributes are the same, it is an intersection (not managed by SQL JOIN)
    if attributes_match(subrelation1.getAttributes(), subrelation2.getAttributes()) :
      self.intersect = True
      return
    else :
      self.intersect = False
    
    # check common attributes
    for attr2 in subrelation2.getAttributes() :
      attr1 = self.getAttribute(attr2.getName(), False)
      # not common, add it to attributes
      if not attr1 :
        self.attributes.append(attr2)
        continue
      # common attributes, check type
      if attr1.getType() == attr2.getType() :
        self.common_attributes_name.append(attr1.getName())
      # attribute with same name but different type
      else :
        self.error(str(attr1)+' in subrelation1 is not the same type as '+str(attr2)+' in subrelation2')
    
  def toSQL(self) :
    if self.intersect :
      return 'SELECT * FROM ('+self.subrelation1.toSQL()+') INTERSECT SELECT * FROM ('+self.subrelation2.toSQL()+')'
    
    using = ''
    if self.common_attributes_name :
      common_columns = '"'+'","'.join(self.common_attributes_name)+'"'
      using = ' USING ('+common_columns+')'
    return 'SELECT * FROM ('+self.subrelation1.toSQL()+') JOIN ('+self.subrelation2.toSQL()+')'+using
