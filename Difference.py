from Relation import Relation



class Difference(Relation):
  def __init__(self, subrelation1, subrelation2):
    # check that arguments are objects of type Relation
    if not isinstance(subrelation1, Relation):
      raise TypeError('subrelation1 argument must be of type Relation')
    if not isinstance(subrelation2, Relation):
      raise TypeError('subrelation2 argument must be of type Relation')
    self.subrelation1 = subrelation1
    self.subrelation2 = subrelation2

    # saves attributes from both arguments
    attributes1 = subrelation1.getAttributes()
    attributes2 = subrelation2.getAttributes()


    # check that attributes are exactly the same
    if len(attributes1) != len(attributes2):
      raise Exception('subrelation1 must have same attributes as subrelation2')
    for attr1, attr2 in zip(attributes1, attributes2):
      if attr1.getName() != attr2.getName() or attr1.getType() != attr2.getType():
        raise Exception('subrelation1 must have same attributes as subrelation2')

    # save correct attributes
    self.setAttributes(attributes1)


  def toSQL(self):
    # query
    return 'Select * FROM (' + self.subrelation1.toSQL()+ ')' + ' EXCEPT SELECT * FROM (' + self.subrelation2.toSQL() + ')'

