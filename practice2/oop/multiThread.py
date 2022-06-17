import time

class RacingCar:
	name = ''

	def __init__(self, name = ''):
		self.name = name

	def run(self):
		for _ in range(5):
			print(f"racing car {self.name} starts run")
			time.sleep(0.1)
	
