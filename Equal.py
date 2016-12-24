from base import *
from Cst import Cst



class Equal(Expression):

	def __init__(self, attr1, attr2):
		self.attr1 = attr1
		self.attr2 = attr2
		self.verifyType()

	def __str__(self):
		return str(self.attr1) + " = " + str(self.attr2)

	def verifyType(self):
		if not isinstance(self.attr1, Attribute):
			raise TypeError("First attribute must be of type Attribute (Column)")

		elif not isinstance(self.attr2, Attribute) and not isinstace(self.attr2, Cst):
			raise TypeError("Second attribute must be of type Attribute or Cst (Constant)")
