from vector import *
import pygame

class Fish:
    def __init__(self, position, velocity, img):
        self.position = position
        self.velocity = velocity
        self.img = pygame.transform.scale(pygame.image.load(img), (100, 40))
    
    def update(self):
        self.velocity = self.screenConfinementBounce()
        self.position = self.position + self.velocity

    def draw(self, screen):
        screen.blit(self.img, (self.position.x, self.position.y))

    def screenConfinementBounce(self):
        #velocity = self.__velocity
        self.position += self.velocity
        if self.position.x > 700 or self.position.x < 0:
            self.velocity = Vector(-self.velocity.x, self.velocity.y)
        elif self.position.y < 0 or self.position.y > 560:
            self.velocity = Vector(self.velocity.x, -self.velocity.y)
        return self.velocity
v="fuck yo self v2"