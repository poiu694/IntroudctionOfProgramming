class Car:
	color = ''
	speed = 0
	count = 0

	def __init__(self, color = 'red', speed = 0):
		self.color = color
		self.speed = speed
		Car.count += 1
	
	def upSpeed(self, value):
		self.speed += value
		if self.speed > 150:
			print('car speed cannot over maximum speed 150')
			self.speed= 150
	
	def downSpeed(self, value):
		self.speed -= value

	def getSpeed(self):
		return self.speed
	
	def getColor(self):
		return self.color
	
	def printInfo(self):
		print(f"car's color : {self.color}, speed : {self.speed} ")

