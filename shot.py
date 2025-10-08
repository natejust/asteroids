import pygame
from circleshape import CircleShape
import constants

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, constants.SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255),
                           (self.position.x,self.position.y),
                             self.radius)

    def update(self, delta_time):
       self.position += self.velocity*delta_time