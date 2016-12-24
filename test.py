# for debug purposes
from pprint import pprint

#""" Test SQLiteRelation
from sqlite import SQLiteRelation

rel = SQLiteRelation('database', 'emp')
#pprint(rel.getSchema())
#"""

#""" Test Project
from Project import Project

rel = Project(['ename', 'empno'], rel)
pprint(rel.getSchema())
#"""

#""" Execute request on database
import sqlite3

sql = rel.toSQL()+';'
database = sqlite3.connect('database.db')
cursor = database.cursor()
tuples = cursor.execute(sql)

pprint(rel.getAttributes())
for t in tuples :
  pprint(t)
#"""
