from base import *
from Equal import Equal



#Alexis lis ça car j'avais qlq chose comme ça en tête mais avec ta structure ça doit etre different 

class Select(Relation):
	def __init__(self, eq, relation):
		self.eq = eq
		self.relation = relation
		self.verify()
		self.req = "SELECT * FROM " + str(self.relation) + " WHERE " + str(self.eq)

	def __str__(self):
		return self.req


	def verify(self):
		if not isinstance(self.eq, Equal):
			raise TypeError("The argument eq has to be an object of type Equal")
		elif not isinstance(self.relation, Relation) and not isinstance(self.relation, Expression):
			raise TypeError("The argument relation has to be and object of type Relation or Expression")
