from Relation import Relation
from functions import *

# Class Select to access constants 
class SelectConstant(Relation) :
  def __init__(self, attribute_name, constant, subrelation) :
    # check and save subrelation
    self.subrelation = check_relation(self, subrelation, 'subrelation')
    
    # schema is unchanged
    self.setAttributes(subrelation.getAttributes())
    
    # checks are made in getAttribute
    self.attribute = self.getAttribute(attribute_name, True, 'subrelation')
    self.constant = str(constant)
  
  def toSQL(self) :
    comparison = '"'+self.attribute.getName()+'"='+"'"+self.constant.replace("'", "\\'")+"'"
    # query
    return 'SELECT * FROM ('+self.subrelation.toSQL()+') WHERE '+comparison
