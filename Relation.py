from pprint import pprint

class Relation :
  # datatypes from https://www.sqlite.org/datatype3.html and FLOAT return by PRAGMA TABLE_INFO()
  valid_types = ['TEXT', 'NUMERIC', 'INTEGER', 'REAL', 'BLOB', 'FLOAT']
  
  def __init__(self, schema) :
    self.setSchema(schema)
  
  def setSchema(self, schema) :
    if not isinstance(schema, dict) :
      raise TypeError('schema argument must be of type dict"')
    
    for name in schema :
      type = schema[name]
      if not type in Relation.valid_types :
        raise TypeError('schema invalid type "'+type+'" for attribute "'+name+'"')
    
    self.schema = schema
  
  def getSchema(self) :
    return self.schema
  
  def getAttributes(self) :
    attributes = []
    for att in self.schema :
      attributes.append(att)
    return attributes
  
  def toSQL(self) :
    raise Exception('method toSQL not implemented here')
