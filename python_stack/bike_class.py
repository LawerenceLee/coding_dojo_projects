
class Bike:
    miles = 0

    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed

    def displayInfo(self):
        print("Price: ${}, Max-Speed: {} mph, Miles: {}".format(
            self.price, self.max_speed, self.miles))

    def ride(self):
        print("Riding")
        self.miles += 10
        return self

    def reverse(self):
        print("Reversing")
        if self.miles == 5:
            self.miles -= 5
        return self


print("Timmy's Bike:")
timmy = Bike(150, 45).ride().ride().ride().reverse().displayInfo()

print("")
print("Roger's Bike")
roger = Bike(1000, 65).ride().ride().reverse().reverse().displayInfo()

print("")
print("Dan's Bike")
dan = Bike(25, 23).reverse().reverse().reverse().displayInfo()
