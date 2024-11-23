import pygame
import random
import math

class Asteroid:
    def __init__(self, speed, screen) -> None:
        size = random.choice([16,32,64])
        self.size = (size, size)
        self.speed = speed
        self.screen = screen
        self.pos = ()
        self.dir = 0
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asteroid.png"), self.size), random.randint(0, 360))
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

        spawn_pos = random.randint(0, 7)
        match spawn_pos:
            case 0:
                self.pos = (random.randint(300,600),0-size)
                self.dir = random.randint(270, 360)
            case 1:
                self.pos = (600,random.randint(0-size,300-size))
                self.dir = random.randint(270, 360)
            case 2:
                self.pos = (600,random.randint(300,600))
                self.dir = random.randint(180, 270)
            case 3:
                self.pos = (random.randint(300,600),600)
                self.dir = random.randint(180, 270)
            case 4:
                self.pos = (random.randint(0-size,300-size),600)
                self.dir = random.randint(90, 180)
            case 5:
                self.pos = (0-size,random.randint(300,600))
                self.dir = random.randint(90, 180)
            case 6:
                self.pos = (0-size,random.randint(0-size,300-size))
                self.dir = random.randint(0, 90)
            case 7:
                self.pos = (random.randint(0-size,300-size),0-size)
                self.dir = random.randint(0, 90)
        
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):
        dir = math.radians(self.dir)
        self.pos = (self.pos[0] + math.sin(dir) * self.speed, self.pos[1] + math.cos(dir) * self.speed)

        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]
    
    def draw(self):
        self.screen.blit(self.image, self.image.get_rect(center=self.rect.center))
        self.mask = pygame.mask.from_surface(self.image)
