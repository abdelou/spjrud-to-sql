import sqlite3

class Relation(object):

	#Class representing the relation (SPJRUD) or table (SQL)
	
	
	#attr is a list of Attribute type objects
	def __init__(self, name, attr):
		self.name = name
		self.attr = attr


	def __str__(self):
		return self.name


class Expression(object):

	#Class used as a base for all type of SPJRUD expressions (So, each Node of the AST)


	def __init__(self, relation):
		self.relation = relation
		
	
class Attribute(object): #Object?
	
	#Class that represents the attributes (SPJRUD) or Columns (SQL)
	
	def __init__(self, name, type):
		self.name = name
		self.type = type
		
	def __str__(self):
		return self.name
	
	def getType(self):
		return self.type

