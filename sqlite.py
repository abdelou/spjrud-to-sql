import sqlite3
from Relation import Relation, Attribute

# for debug purposes
from pprint import pprint

def getAttributesFromTable(database, table) :
  cursor = database.cursor()
  infos = cursor.execute('PRAGMA table_info('+table+');')
  
  attributes = []
  for tup in infos :
    attributes.append(Attribute(tup[1], tup[2]))
  
  return attributes or False

class SQLiteRelation(Relation) :
  def __init__(self, database_name, relation_name) :
    database = sqlite3.connect(database_name+'.db')
    s = getAttributesFromTable(database, relation_name)
    if not s :
      raise Exception('Relation "'+relation_name+'" does not exists in database "'+database_name+'"')
    self.setAttributes(s)
    self.relation_name = relation_name
  def toSQL(self) :
    return 'SELECT * FROM '+self.relation_name
