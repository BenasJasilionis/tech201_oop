from snake import Snake
# Polymorphism - can change inherited class variables and methods in instance class without affecting the class variables or methods for other objects

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.cold_blooded = True
        self.venom = False

    def digest_large_prey(self):
        print("Ok, let me get the stretchy pants")

    def constrict(self):
        print("Squeeeeeeeeeeze")

    def climb(self):
        print("Up we go")

    def shed_skin(self):
        print("I'm growing out of this now")

peter = Python()
peter.breathe()
peter.use_tongue_to_smell()
peter.hunt()
peter.shed_skin()