import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        asteroid_a_velocity = self.velocity.rotate(random_angle)
        asteroid_b_velocity = self.velocity.rotate(-random_angle)
        asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid_a.velocity = 1.2 * asteroid_a_velocity;
        asteroid_b.velocity = 1.2 * asteroid_b_velocity;


         
