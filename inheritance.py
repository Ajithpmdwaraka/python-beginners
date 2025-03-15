class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod    
    def stop():
        print("Car stopped")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        print(name, "is one of the toyota cars")


Car1 = ToyotaCar("Inova")   
Car1.start()
        
            