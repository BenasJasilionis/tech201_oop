# OOP Four Pillars
Object orientated programming is a programming style which is focuses programming around objects and classes rather than functions and logic. OOP focuses on the objects in use rather than the logic required to manipulate them
# The 4 pillars of OOP - Abstraction
Abstraction aims to reduce complexity and isolate the impact of change. The idea of abstraction is the user only needs to be able to use the code, they don't need to know/ interact with the logic underlying it.
````python
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

cat = Animal()
cat.eat() # Output = Nom Nom Nom
````
* Here we have a `class` `Animal` and from it we have made the object `cat`.
* Abstraction is at play here because when we call the `cat` to eat, we don't have to write out the whole function, we only need to know to type `.eat`
* To achieve our goal, we do not need to know how to write the `method`, only how to use it which is the essence of `abstraction`

**Note - Abstraction isn't only implemented in OOP, simply using functions is an example of abstraction**

# Inheritance
Inheritance is concerned with eliminating redundant code, and this is achieved by allowing `classes` to `inherit` `class variables` and `class methods` from the base class:
* In order for a new `class` to inherit the base `classes`: features, the following syntax must be used:

```
from <file name> import <ClassName>

class NewClassName(OldClassName):
         def __init__(self):
         super().__init__()
```
* Following this code, the new class can be created as normal, and it will have access to the `base classes'` attributes:
````python
from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.hear_chambers = [3, 4]
        self.amniotic_eggs = None
        self.venom = False

    def seek_heat(self):
        print("It's chilly outside, where is the sun?")

    def hunt(self):
        print("Wait, wait, wait....Pounce")

    def use_venom(self):
        print("If I have got it, I am going to use it")

    def attract_through_scent(self):
        print("Time to spray some eut de toilette")


jeremy_the_reptile = Reptile() 
jeremy_the_reptile.breathe()   # Output = One breath in and one breath out
jeremy_the_reptile.hunt()      # Output = Wait, wait, wait....Pounce
````
* As can be seen the `Animal class` is `imported`, which allows the new `class Reptile` to inherit the base attributes.
* The object `jeremy_the_reptile` which has been `instantiated` has access to the `class variables` and `class methods` of both `Animal` and `Reptile` 





- Abstraction
- Inheritance
- Encapsulation
- Polymorphism















![](OOP.png.png)