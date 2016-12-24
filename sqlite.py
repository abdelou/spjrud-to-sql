import sqlite3
from Relation import Relation

# for debug purposes
from pprint import pprint

def get_schema(database, table) :
  cursor = database.cursor()
  infos = cursor.execute('PRAGMA table_info('+table+');')
  
  schema = {}
  for tup in infos :
    column_name = tup[1]
    column_type = tup[2]
    schema[column_name] = column_type
  
  return schema or False

class SQLiteRelation(Relation) :
  def __init__(self, database_name, relation_name) :
    database = sqlite3.connect(database_name+'.db')
    s = get_schema(database, relation_name)
    if not s :
      raise Exception('Relation "'+relation_name+'" does not exists in database "'+database_name+'"')
    self.setSchema(s)
    self.relation_name = relation_name
  def toSQL(self) :
    return 'SELECT * FROM '+self.relation_name
