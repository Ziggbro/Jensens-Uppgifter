
class Car:

    def __init__(self, brand, model, year, speed = 0.0):

        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0.0


    def drive(self, input_speed):
        self.speed = input_speed

    def stop(self):
        self.speed = 0.0



car1 = Car("Honda", "Civic", 2021)
car2 = Car("Toyota", "Corolla", 2022)

car1.drive(50)
print("Bil 1 hastighet:", car1.speed)

car2.drive(70)
print("Bil 2 hastighet:", car2.speed)

car1.stop()
print("Bil 1 hastighet efter stop:", car1.speed)
print("Bil 2 hastighet:", car2.speed)




