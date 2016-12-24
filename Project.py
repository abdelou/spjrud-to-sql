from Relation import Relation


class Project(Relation) :
  def __init__(self, attributes, subrelation) :
    if not isinstance(subrelation, Relation) :
      raise TypeError('subrelation argument must be of type Relation"')
    self.schema = {}
    self.subrelation = subrelation
    subschema = subrelation.getSchema()
    for att in attributes :
      if not att in subschema :
        raise Exception('Sub-Relation of Project has no attribute "'+att)
      self.schema[att] = subschema[att]
  def toSQL(self) :
    att = ','.join(self.getAttributes())
    return 'SELECT '+att+' FROM ('+self.subrelation.toSQL()+')'
