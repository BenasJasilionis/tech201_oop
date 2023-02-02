from animal import Animal
# Inheritance eliminates redundant code
# Class reptile inherits class variables and methods from class Animal. Can still add new class variables and methods specific to reptile
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


# Super relates back to base class (Animal), tells python to use all the class varaibles and methods from base class (Animal)

# jeremy_the_reptile = Reptile()
#
# jeremy_the_reptile.breathe()
# jeremy_the_reptile.hunt()
# jeremy_the_reptile.eat()
