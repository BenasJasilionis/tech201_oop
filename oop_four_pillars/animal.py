# Abstraction - when im using the method, don't need to know how it works, but its within the same file - don't need to retype the function- functions are essentially abstraction

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("Find a mate")

    def move(self):
        print("Onwards and Upwards")

# Because the .breathe method has been abstracted, don't see its logic, but know how to use it
# Abstraction - don't understand all the behind the scenes, just know how to use whats needed
cat = Animal()
#cat.eat()
