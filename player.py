import pygame
import math

class Player:
    def __init__(self, size, speed, rot_speed, screen) -> None:
        self.size = size
        self.speed = speed
        self.rot_speed = rot_speed
        self.screen = screen
        self.pos = (300-size[0]/2, 300-size[1]/2)
        self.dir = ()
        self.rot = 0

        self.rect = pygame.Rect
        self.rot_rect = pygame.Rect

        self.image = pygame.image.load("player.png")

    def transform(self, inputs):
        self.rot += inputs[1] * self.rot_speed
        self.dir = (math.cos(math.radians(self.rot)), -math.sin(math.radians(self.rot)))

        norm = (self.dir[0]**2 + self.dir[1]**2)**0.5
        if self.dir[0] != 0 and self.dir[1] != 0: self.dir = (self.dir[0]/norm, self.dir[1]/norm)
        self.pos = (self.pos[0] + self.dir[0] * self.speed * inputs[0], self.pos[1] + self.dir[1] * self.speed * inputs[0])

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def draw(self):
        image = pygame.transform.rotate(self.image, self.rot-90)
        self.screen.blit(image, image.get_rect(center=self.rect.center))
        ##########################################################################
        # FOR DEBUGGING PURPOSES
        pygame.draw.rect(self.screen, "green", self.rect, 1)
        ##########################################################################

#class Bullet:
#    def __init__(self) -> None:
        
