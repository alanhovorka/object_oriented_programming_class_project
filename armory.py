from room import Room

class Armory(Room):
	"""docstring for Armory"""
	def __init__(self, name):
		super().__init__(name)
		self.description = """\n
		#insert description
		\n"""
		self.contents = []
		self.doors = {"": "", "": ""}
