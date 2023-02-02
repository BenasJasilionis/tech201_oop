# Object Oriented Programming (OOP)

# Everything in OOP is an object and objects are modelled against real world objects
# Make templates of an object that have attributes (variables) and behaviours/methods (functions)
# Classes are the templates we use to create objects
# Classes are a way of bringing both the data and functionality of our code together

# Create a class
#When naming classes no underscores, use capitals
# Functions outside of scope of class, methods inside
class Dog:

    animal_kind = "Canine" # class variable


    def bark(self): # method
        return "woof"

# self - "I'm referring to the current class". e.g. class dog
# self tells python where to get the variable from- knows to look into the class

#print(Dog.animal_kind)
#print(Dog.bark()) ## ERROR

# Instantiation of a class - making an object from a  class (the template)
# Need to instantiate an object ot be able to use methods
# Objects can be instantiated from class templates in other files
# Class variables can only be accessed through the class or the class object

fido = Dog()
lassie = Dog()

print(type(fido))        # Output = <class '__main__.Dog'>
print(type(lassie))      # Output = <class '__main__.Dog'>
print(fido.animal_kind)  # Output = Big Dog
print(lassie.animal_kind)# Output = Big Dog
print(fido.bark())       # Output = woof

# Can overwrite class variables for individual objects, without affecting other object's - instance variable
# Objects are separate from one another
fido.animal_kind = "Big Dog"

print(fido.animal_kind)   # Output = Big Dog
print(lassie.animal_kind) # Output = Canine

# Can change variables at a class level as well
Dog.animal_kind = "Dolphin"
print(fido.animal_kind)   # Output = Dolphin
print(lassie.animal_kind) # Output = Dolphin

# Overwriting instance variables takes priority over class variables for an individual object

lassie.animal_kind = "Turtle"
Dog.animal_kind_ = "Dolphin"
print(lassie.animal_kind) # Output = Turtle