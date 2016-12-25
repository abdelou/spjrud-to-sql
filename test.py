# for debug purposes
from pprint import pprint

def exec_request(relation) :
  import sqlite3
  
  sql = relation.toSQL()+';'
  pprint(sql)
  
  database = sqlite3.connect('database.db')
  cursor = database.cursor()
  tuples = cursor.execute(sql)
  
  print_relation(relation.getAttributesName(), tuples)

#"""

def print_relation(attributes, tuples) :
  # get data and convert them to str
  rows = []
  for t in tuples :
    new_row = []
    for val in t :
      new_row.append(str(val))
    rows.append(new_row)
  
  # get max length for each column
  max = {}
  for attr in attributes :
    max[attr] = len(attr)
  
  for row in rows :
    for attr, val in zip(attributes, row) :
      l = len(val)
      if l > max[attr] :
        max[attr] = l
  
  # create separator
  separator = '+-'
  for attr in attributes :
    separator = separator + pad_left('', max[attr], '-') + '-+-'
  # remove last "-"
  separator = separator[:-1]
  # start printing
  print separator
  # print header
  line = '| '
  for attr in attributes :
    line = line + pad_left(attr, max[attr]) + ' | '
  # remove last " "
  line = line[:-1]
  print line
  print separator
  # print data
  for row in rows :
    line = '| '
    for attr, val in zip(attributes, row) :
      line = line + pad_left(val, max[attr]) + ' | '
    # remove last " "
    line = line[:-1]
    print line
  
  print separator

def pad_left(string, size, character=' ') :
  l = len(string)
  p = ''
  for i in range(l, size) :
    p = p+character
  
  return p+string

#""" Test SQLiteRelation
from sqlite import SQLiteRelation

emp = SQLiteRelation('database', 'emp')
dept = SQLiteRelation('database', 'dept')
#pprint(rel.getAttributesName())
#"""

""" Test Rename
from Rename import Rename

rel = Rename('ename', 'E e', rel)
pprint(rel.getAttributesName())
#"""

""" Test Project
from Project import Project

rel = Project(['ename', 'empno'], rel)
#rel = Project(['ename'], rel)
#rel = Project(['E e'], rel)
#pprint(rel.getAttributesName())
#"""

""" Test SelectAttribute
from SelectAttribute import SelectAttribute
# not comparable attributes
rel = SelectAttribute('ename', 'empno', rel)
#pprint(rel.getAttributesName())
#"""
""" Test SelectAttribute
from SelectAttribute import SelectAttribute
# comparable attributes
rel = SelectAttribute('ename', 'job', rel)
#pprint(rel.getAttributesName())
#"""

""" Test SelectConstant
from SelectConstant import SelectConstant
# comparables attributes
rel = SelectConstant('E e', 'BLAKE', rel)
#pprint(rel.getAttributesName())
#"""

""" Test Union
from Union import Union
from SelectConstant import SelectConstant

rel1 = SelectConstant('ename', 'BLAKE', rel)
rel2 = SelectConstant('ename', 'JONES', rel)
rel = Union(rel1, rel2)
#pprint(rel.getAttributesName())
#"""

#""" Test Join
from Join import Join

from SelectConstant import SelectConstant

rel1 = SelectConstant('ename', 'BLAKE', emp)

rel2 = Join(rel1, dept)
exec_request(rel2)
#"""



