from base import Expression


class Cst(Expression):

	#Class that represents a constant (ex: a constant inside a column in a table)


	#On utilise un tuple pour representer la valeur et le type de cet valeur?
	def __init__(self, data):
		self.data = data


