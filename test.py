# for tests purposes
from tests.functions import exec_request
from tests.database import create_database, delete_database
# import all operators from SPJRUD
from SPJRUD.SelectAttribute import SelectAttribute
from SPJRUD.SelectConstant import SelectConstant
from SPJRUD.Project import Project
from SPJRUD.Join import Join
from SPJRUD.Rename import Rename
from SPJRUD.Union import Union
from SPJRUD.Difference import Difference
# SQLite
from sqlite import SQLiteRelation
# manual creation
from Relation import Relation, Attribute
from SPJRUD.functions import str_attributes
# for arguments
import sys

l = len(sys.argv)
if l < 2 :
  print "Usage : python test.py TEST_NUMBER"
  exit(0)
try :
  test = int(sys.argv[1])
except ValueError :
  print "Usage : python test.py TEST_NUMBER"
  exit(0)

# create an SQLite test database
DB_NAME = 'test_db'
create_database(DB_NAME)
# get attributes from database
emp = SQLiteRelation(DB_NAME, 'emp')
dept = SQLiteRelation(DB_NAME, 'dept')

# manually create attributes, SQL can't be generated but errors will be checked
man_rel = Relation([
Attribute('name', 'TEXT'),
Attribute('age', 'INTEGER')
])
if test == 0 :
  print str_attributes(man_rel.getAttributes())

# test SQLiteRelation
if test == 1 :
  rel = emp
if test == 2 :
  rel = dept


# Test SelectAttribute
if test == 10 :
  # error : attribute does not exists
  rel = SelectAttribute('ename', 'nonexistant', emp)
if test == 11 :
  # error : not comparable attributes
  rel = SelectAttribute('ename', 'empno', emp)
if test == 12 :
  # working : comparable existing attributes
  rel = SelectAttribute('ename', 'job', emp)


# Test SelectConstant
if test == 20 :
  # error : attribute does not exists
  rel = SelectConstant('nonexistant', 'my_constant', emp)
if test == 21 :
  # working : existing attribute
  rel = SelectConstant('ename', 'BLAKE', emp)


# Test Project
if test == 30 :
  # error : attribute does not exists
  rel = Project(['ename', 'nonexistant'], emp)
if test == 31 :
  # working : existing attribute
  rel = Project(['ename', 'empno'], emp)


# Test Join
if test == 40 :
  # error : 2 attributes with same name but different types
  rel1 = Rename('ename', 'common', emp)
  rel2 = Rename('empno', 'common', emp)
  rel = Join(rel1, rel2)
if test == 41 :
  # common column "deptno"
  rel = Join(emp, dept)
if test == 42 :
  # no common column, cartesian product
  rel1 = SelectConstant('ename', 'BLAKE', emp)
  rel2 = Rename('deptno', 'deptno2', dept)
  rel = Join(rel1, rel2)
if test == 43 :
  # all common column, intersection
  rel1 = Union(SelectConstant('ename', 'BLAKE', emp), SelectConstant('ename', 'JONES', emp))
  rel2 = Union(SelectConstant('ename', 'BLAKE', emp), SelectConstant('ename', 'SMITH', emp))
  rel = Join(rel1, rel2)


# Test Rename
if test == 50 :
  # error : attribute does not exists
  rel = Rename('nonexistant', 'newname', emp)
if test == 51 :
  # error : new_name already exists
  rel = Rename('ename', 'empno', emp)
if test == 52 :
  # working
  rel = Rename('ename', 'Name', emp)


# Test Union
if test == 60 :
  # error : one attribute not common
  rel1 = Project(['ename', 'job'], emp)
  rel2 = Project(['job'], emp)
  rel = Union(rel1, rel2)
if test == 61 :
  # error : all differents attributes
  rel1 = Project(['ename'], emp)
  rel2 = Project(['job'], emp)
  rel = Union(rel1, rel2)
if test == 62 :
  # error : one attribute with same name but different type
  rel1 = Project(['ename'], emp)
  rel2 = Rename('deptno', 'ename', Project(['deptno'], emp))
  rel = Union(rel1, rel2)
if test == 63 :
  # working
  rel1 = SelectConstant('ename', 'BLAKE', emp)
  rel2 = SelectConstant('ename', 'SMITH', emp)
  rel = Union(rel1, rel2)


# Test Difference
if test == 70 :
  # error : one attribute not common
  rel1 = Project(['ename', 'job'], emp)
  rel2 = Project(['job'], emp)
  rel = Difference(rel1, rel2)
if test == 71 :
  # error : all differents attributes
  rel1 = Project(['ename'], emp)
  rel2 = Project(['job'], emp)
  rel = Difference(rel1, rel2)
if test == 72 :
  # error : one attribute with same name but different type
  rel1 = Project(['ename'], emp)
  rel2 = Rename('deptno', 'ename', Project(['deptno'], emp))
  rel = Difference(rel1, rel2)
if test == 73 :
  # working
  rel1 = emp
  rel2 = Union(SelectConstant('ename', 'SMITH', emp), SelectConstant('ename', 'ALLEN', emp))
  rel = Difference(rel1, rel2)

# execute test request and delete database
try :
  exec_request(DB_NAME, rel)
except NameError :
  print 'No test with number "'+str(test)+'"'
delete_database(DB_NAME)
