from Car import Car
from classInheritance import Truck

car1 = Truck('chars', 50, 10)
car2 = Truck('stri', 30, 140)

print(f"tot car : {Car.count}")

car1.printInfo()
print(f"CAR WEIGHT : {car1.weight}")

car2.printInfo()
print(f"CAR WEIGHT : {car2.weight}")

