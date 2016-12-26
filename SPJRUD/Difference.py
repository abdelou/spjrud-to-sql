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
      att1 = str(attributes1)
      att2 = str(attributes2)
      raise Exception('subrelation1 must have same attributes as subrelation2. Your subrelation1 attributes are:/n' + att1 + '/nWhile your subrelation2 attributes are:/n' + att2)
    for attr1, attr2 in zip(attributes1, attributes2):
      if attr1.getName() != attr2.getName() or attr1.getType() != attr2.getType():
        for att1, att2 in zip(attributes1, attributes2):
          msg1 = '' + att1.getName() + ':' + att1.getType() + '/n'
          msg2 = '' + att2.getName() + ':' + att2.getType() + '/n'
        raise Exception('subrelation1 must have same attributes as subrelation2. Your subrelation 1 attributes are:/n' + msg1 + '/nWhile your subrelation2 attributes are:/n' + msg2)

    # save correct attributes
    self.setAttributes(attributes1)


  def toSQL(self):
    # query
    return 'Select * FROM (' + self.subrelation1.toSQL()+ ')' + ' EXCEPT SELECT * FROM (' + self.subrelation2.toSQL() + ')'

