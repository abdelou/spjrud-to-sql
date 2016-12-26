# for debug purposes
from tests.functions import exec_request
from tests.database import create_database, delete_database

DB_NAME = 'test'

# create a test database
create_database(DB_NAME)

#""" Test SQLiteRelation
from sqlite import SQLiteRelation

emp = SQLiteRelation(DB_NAME, 'emp')
dept = SQLiteRelation(DB_NAME, 'dept')
#exec_request(DB_NAME, emp)
#exec_request(DB_NAME, dept)
#"""

""" Test SelectAttribute
from SPJRUD.SelectAttribute import SelectAttribute

# not comparable attributes
#rel = SelectAttribute('ename', 'empno', emp)

# comparable attributes
rel = SelectAttribute('ename', 'job', emp)

exec_request(DB_NAME, rel)
#"""


""" Test SelectConstant
from SPJRUD.SelectConstant import SelectConstant

# comparables attributes
rel = SelectConstant('ename', 'BLAKE', emp)

exec_request(DB_NAME, rel)
#"""


""" Test Project
from SPJRUD.Project import Project

rel = Project(['ename', 'empno'], emp)

exec_request(DB_NAME, rel)
#"""


#""" Test Join
from SPJRUD.Join import Join

from SPJRUD.SelectConstant import SelectConstant
from SPJRUD.Rename import Rename

rel = SelectConstant('ename', 'BLAKE', emp)

#rel = Join(rel, dept)
rel = Join(rel, Rename('deptno', 'deptno2', dept))

exec_request(DB_NAME, rel)
#"""


""" Test Rename
from SPJRUD.Rename import Rename

rel = Rename('ename', 'Name', emp)
exec_request(DB_NAME, rel)
#"""


""" Test Union
from SPJRUD.Union import Union
from SPJRUD.SelectConstant import SelectConstant

rel1 = SelectConstant('ename', 'BLAKE', emp)
rel2 = SelectConstant('ename', 'JONES', emp)

rel = Union(rel1, rel2)

exec_request(DB_NAME, rel)
#"""


delete_database(DB_NAME)

