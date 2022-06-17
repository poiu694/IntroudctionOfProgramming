from Car import Car

# car test #
car1 = Car()
car1.printInfo()
print(car1.getSpeed())
car1.upSpeed(50)
print(car1.getSpeed())
car1.downSpeed(3)
print(car1.getSpeed())
car1.upSpeed(50)
print(car1.getSpeed())
car1.upSpeed(50)
print(car1.getSpeed())
car1.upSpeed(50)
print(car1.getSpeed())

# car2 test #
car2 = Car('blue', 50)
car2.printInfo()

# Car count test #
print(f"tot car count : {Car.count}")
