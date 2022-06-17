from multiThread import RacingCar
import threading

car1 = RacingCar('자동차 1')
car2 = RacingCar('자동차 2')
car3 = RacingCar('자동차 3')

th1 = threading.Thread(target = car1.run)
th2 = threading.Thread(target = car2.run)
th3 = threading.Thread(target = car3.run)

th1.start()
th2.start()
th3.start()
