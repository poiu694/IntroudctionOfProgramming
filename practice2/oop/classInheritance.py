from Car import Car

class Truck(Car):
	weight = 0
	
	def __init__(self, name = '', speed = 0, weight = 0):
		self.name = name
		self.speed= speed
		self.weight = weight
		Car.count += 1
	
	def getWeight(self):
		return self.weight
