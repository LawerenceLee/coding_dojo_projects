
class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()

    def display_all(self):
        print("Price: ${}, Speed: {} mph, Fuel: {}, Milage: {} mpg, Tax: {}".format(
            self.price, self.speed, self.fuel, self.mileage, self.tax))


toyota_prius = Car(2000, 35, "full", 15)
range_rover = Car(2000, 5, "not Full", 105)
ford_raptor = Car(2000, 15, "Kind of Full", 95)
gremlin = Car(2000, 25, "Full", 25)
jeep = Car(2000, 45, "Empty", 25)
nissan = Car(2000000, 35, "Empty", 15)
