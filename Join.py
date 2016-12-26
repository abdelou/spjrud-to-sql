from Relation import Relation
from copy import deepcopy


class Join(Relation) :
  def __init__(self, subrelation1, subrelation2) :
    # check that arguments are objects of type Relation
    if not isinstance(subrelation1, Relation) :
      raise TypeError('subrelation1 argument must be of type Relation"')
    if not isinstance(subrelation2, Relation) :
      raise TypeError('subrelation2 argument must be of type Relation"')
    self.subrelation1 = subrelation1
    self.subrelation2 = subrelation2
    
    # copy at least attributes from attributes1
    self.setAttributes(deepcopy(subrelation1.getAttributes()))
    # make list of common attributes for future use
    self.common_attributes_name = []
    
    for attr2 in subrelation2.getAttributes() :
      attr1 = self.getAttribute(attr2.getName(), False)
      if attr1 :
        # common attribute
        if attr1.getType() == attr2.getType() :
          self.common_attributes_name.append(attr1.getName())
        # attribute with same name but different type
        else :
          raise Exception(attr1+' in relation 1 is not the same type as '+attr2+' in relation 2')
      # different attribute name, add it
      else :
        self.attributes.append(attr2)
  
  def toSQL(self) :
    common_columns = '"'+'","'.join(self.common_attributes_name)+'"'
    
    # query
    return 'SELECT * FROM ('+self.subrelation1.toSQL()+') JOIN ('+self.subrelation2.toSQL()+') USING ('+common_columns+')'
