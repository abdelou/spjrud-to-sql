from Relation import Relation
from Functions import *



class Difference(Relation):
  def __init__(self, subrelation1, subrelation2):
    # check that arguments are objects of type Relation
    check_relation(subrelation1, 1)
    check_relation(subrelation2, 2)
    self.subrelation1 = subrelation1
    self.subrelation2 = subrelation2

    # saves attributes from both arguments
    attributes1 = subrelation1.getAttributes()
    attributes2 = subrelation2.getAttributes()

    # check that attributes are exactly the same
    check_attributes_match(attributes1, attributes2)
    
    # save correct attributes
    self.setAttributes(attributes1)


  def toSQL(self):
    # query
    return 'Select * FROM (' + self.subrelation1.toSQL()+ ')' + ' EXCEPT SELECT * FROM (' + self.subrelation2.toSQL() + ')'

