from fish import *
from vector import *
import random 

class Flok:

    def __init__(self, n):
        self.flertal = []
        
        for i in range(n):
            position = Vector(random.randint(0,420), random.randint(0,420))
            velocity = Vector(2, 3)
            self.flertal.append(Fish(position, velocity, "fisk.png"))
        
    
    def update(self):   
        for fish in self.flertal:
            fish.update()

    def draw(self, screen):
        for fish in self.flertal:
            fish.draw(screen)


            