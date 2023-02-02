# Initialisation

# Initialisation -> Relates to setting a particular data for an instance of a class/object - differentiating the objects
#Instantiation -> The creation of an instance of an object

class Dog:


    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()


    def bark(self):
        return "woof"

# __init__ = double underscores,stands for initialisation - dunda init
# Now wont lets us make a new 'dog' object without passing arguments for name and colour

fido = Dog("Fido", "Brown")

print(fido.colour)  # Output = Brown
print(fido.name)    # Output = Fido

#__init__ makes it so class variables cannot be changed outside of the class
# Initialising a class with class variables is good practice
