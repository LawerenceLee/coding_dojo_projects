
class Product():
    status = "for sale"

    def __init__(self, item_name, price, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand

    def Sell(self):
        self.status = "sold"
        return self

    def Add_tax(self, tax):
        return self.price + self.price * tax

    def Return(self, reason):
        if "defective" in reason.lower():
            self.status = "defective"
            self.price = 0
        elif "in box" in reason.lower():
            self.status = "like new"
        elif "opened" in reason.lower():
            self.status = "used"
            self.price = self.price - self.price * 0.2
        return self

    def Display(self):
        print("Name: {}, Price: ${}, Weight: {} lbs, Brand: {}, Status: {}".format(
            self.item_name, self.price, self.weight, self.brand, self.status))


toy_train = Product("Toy Train", 10, 10, "Tyco")
toy_train.Sell().Display()
toy_train.Return("defective").Display()

print("")

lipstick = Product("Lipstick", 15, 0.09, "Revlon")
lipstick.Sell().Display()
lipstick.Return("in box").Display()

print("")

beating_stick = Product("Beating Stick", 5, 1, "Bad Parent CO.")
beating_stick.Sell().Display()
beating_stick.Return("opened").Display()
