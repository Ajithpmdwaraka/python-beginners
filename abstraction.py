class Car:
    
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clt = False
    
    def startCar(self):
        if not self.acc:
            print("Car is not accelerating")
        else:
            print("Car is accelerating")

c1 = Car()
c1.startCar()
