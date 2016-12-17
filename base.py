class Relation(object):

	#Class representing the relations (SPJRUD) or table (SQL)

	def __init__(self, name, attr):
		self.name = name
		self.attr = attr


	def __str__(self):
		return self.name


class Expression(object):

	#Class used as a base for all type of SPJRUD expressions


	def __init__(self, relation):
		self.relation = relation


