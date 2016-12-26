# for debug purposes
from pprint import pprint
from tests.functions import exec_request
from tests.database import create_database, delete_database

create_database('test')
#""" Test SQLiteRelation
from sqlite import SQLiteRelation

emp = SQLiteRelation('test', 'emp')
dept = SQLiteRelation('test', 'dept')
#pprint(rel.getAttributesName())
#"""

""" Test Rename
from Rename import Rename

rel = Rename('ename', 'E e', rel)
pprint(rel.getAttributesName())
#"""

#""" Test Project
from SPJRUD.Project import Project

rel = Project(['ename', 'empno'], emp)
#rel = Project(['ename'], rel)
#rel = Project(['E e'], rel)
exec_request('test', rel)
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

""" Test Join
from Join import Join

from SelectConstant import SelectConstant
from Rename import Rename

rel1 = SelectConstant('ename', 'BLAKE', emp)

rel2 = Join(rel1, Rename('deptno', 'Numero de dep', dept))
exec_request(rel2)
#"""

delete_database('test')

