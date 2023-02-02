from reptile import Reptile
# Encapsulation, hide inner workings from the user, while allowing methods to be used. Unlike abstraction, in encapsulation the inner workings are in a completely different file, so you cant even see the logic if you want to.
# Can only do encapsulation via inheritance
class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    def use_tongue_to_smell(self):
        print("Do I say it smells or tastes nice?")


sidney = Snake()
#sidney.seek_heat()