from vector import *
from boid import Boid
import pygame

boid = Boid()

class Fish:
    def __init__(self, position, velocity, img):
        self.position = position
        self.velocity = velocity
        self.img = pygame.transform.scale(pygame.image.load(img), (30, 12))
    
    def update(self, flock_fishes):
        sep = boid.separation(self, flock_fishes)
        ali = boid.alignment(self, flock_fishes)
        coh = boid.cohesion(self, flock_fishes)

        self.velocity += sep + ali + coh
        self.velocity = self.velocity.limit(5)
        self.velocity = self.screenConfinementBounce()
        self.position += self.velocity

    def draw(self, screen):
        screen.blit(self.img, (self.position.x, self.position.y))

    def screenConfinementBounce(self):
        self.position += self.velocity
        if self.position.x > 700 or self.position.x < 0:
            self.velocity = Vector(-self.velocity.x, self.velocity.y)
        elif self.position.y < 0 or self.position.y > 560:
            self.velocity = Vector(self.velocity.x, -self.velocity.y)
        return self.velocity