from Relation import Relation

class check_attributes_match(object):
  def __init__(self, attributes1, attributes2):
    self.attributes1 = attributes1
    self.attributes2 = attributes2
    check()

  def check(self):
    if len(attributes1) != len(attributes2):
      att1 = str(attributes1)
      att2 = str(attributes2)
      raise Exception('subrelation1 must have same attributes as subrelation2. Your subrelation1 attributes are:\n' + att1 + '\nWhile your subrelation2 attributes are:\n' + att2)
    for attr1, attr2 in zip(attributes1, attributes2):
      if attr1.getName() != attr2.getName() or attr1.getType() != attr2.getType():
        for att1, att2 in zip(attributes1, attributes2):
          msg1 = '' + att1.getName() + ':' + att1.getType() + '\n'
          msg2 = '' + att2.getName() + ':' + att2.getType() + '\n'
        raise Exception('subrelation1 must have same attributes as subrelation2. Your subrelation 1 attributes are:/n' + msg1 + '\nWhile your subrelation2 attributes are:\n' + msg2)


class check_relation(object):
  def __init__(self, subrelation, num = 1):
    self.subrelation = subrelation
    self.num = num
    check()

  def check(self):
    if not isinstance(self.subrelation, Relation):
      raise TypeError('Argument ' + self.num + 'must be an object of type Relation')