class SuperClass:
	def printMethod(self):
		raise NotImplementedError()


class SubClass1(SuperClass):
	def printMethod(self):
		print("Override super class")

class SubClass2(SuperClass):
	pass
