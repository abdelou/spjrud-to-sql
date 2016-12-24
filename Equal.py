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
			raise TypeError("Le premier attribute doit etre un objet de type Attribute (Colonne)")

		elif not isinstance(self.attr2, Attribute) and not isinstace(self.attr2, Cst):
			raise TypeError("Le deuxieme attribute doit etre un objet de type Attribute ou Cst (constante)")