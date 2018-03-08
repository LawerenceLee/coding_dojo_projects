class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print("Health: {}".format(self.health))


class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print("I am a dragon")


print("AMY")
amy = Animal("Amy", health=34)
amy.walk().walk().walk().run().run().display_health()
print("")

print("FIDO")
fido = Dog("FIDO")
fido.walk().walk().run().run().pet().display_health()
# fido.fly()  AttributeError: 'Dog' object has no attribute 'fly'
print("")

print("DRAGY")
dragy = Dragon("Dragy")
dragy.display_health()
print("")

print("ROGER")
roger = Animal("Roger", 432)
roger.display_health()
# roger.fly()  AttributeError: 'Animal' object has no attribute 'fly'
# roger.pet()  AttributeError: 'Animal' object has no attribute 'pet'