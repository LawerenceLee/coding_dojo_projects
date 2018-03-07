class Store:

    def __init__(self, product_lst, location, owner):
        self.product_lst = product_lst
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.product_lst.append(product)
        return self

    def remove_product(self, product):
        try:
            self.product_lst.remove(product)
        except ValueError as e:
            print(e)
        return self

    def inventory(self):
        for item in self.product_lst:
            print(item)


dojo = Store(
    ["toy", "makeup", "chicken"], "1920 Zanker Rd. San Jose, CA", "Mr. Jimmy")
dojo.inventory()
print("")
dojo.add_product("Rooster").inventory()
print("")
dojo.remove_product("rabbit")
print("")
dojo.remove_product("toy").inventory()
