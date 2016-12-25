# for debug purposes
from pprint import pprint

#""" Test SQLiteRelation
from sqlite import SQLiteRelation

rel = SQLiteRelation('database', 'emp')
#pprint(rel.getAttributesName())
#"""

#""" Test Rename
from Rename import Rename

rel = Rename('ename', 'E e', rel)
pprint(rel.getAttributesName())
#"""

""" Test Project
from Project import Project

rel = Project(['ename', 'empno'], rel)
rel = Project(['ename'], rel)
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

#""" Test SelectConstant
from SelectConstant import SelectConstant
# comparables attributes
rel = SelectConstant('E e', 'BLAKE', rel)
#pprint(rel.getAttributesName())
#"""


#""" Execute request on database
import sqlite3

sql = rel.toSQL()+';'
pprint(sql)

database = sqlite3.connect('database.db')
cursor = database.cursor()
tuples = cursor.execute(sql)

pprint(rel.getAttributesName())
for t in tuples :
  pprint(t)
#"""
