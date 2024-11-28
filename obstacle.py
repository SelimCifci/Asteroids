import pygame
import random
import math

class Asteroid:
    def __init__(self, speed, screen, new, pos=(), rot=0, size=0) -> None:
        # Chooses a random self.size from the three choices
        if new: self.size = random.choice([16,32,64])
        else: self.size = size
        self.speed = speed
        self.screen = screen
        self.pos = ()
        self.dir = 0
        # Saves a scaled and rotated graphic
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asteroid.png"), (self.size, self.size)), random.randint(0, 360))
        # Creates a mask
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

        # If the asteroid is a new one, chooses a random spawn point (0 -> right half of top side, 1 -> top half of right side ... clockwise)
        if new:
            spawn_pos = random.randint(0, 7)
            match spawn_pos:
                # Sets the spawn point and direction to the corresponding values
                case 0:
                    self.pos = (random.randint(300,600),0-self.size)
                    self.dir = random.randint(270, 360)
                case 1:
                    self.pos = (600,random.randint(0-self.size,300-self.size))
                    self.dir = random.randint(270, 360)
                case 2:
                    self.pos = (600,random.randint(300,600))
                    self.dir = random.randint(180, 270)
                case 3:
                    self.pos = (random.randint(300,600),600)
                    self.dir = random.randint(180, 270)
                case 4:
                    self.pos = (random.randint(0-self.size,300-self.size),600)
                    self.dir = random.randint(90, 180)
                case 5:
                    self.pos = (0-self.size,random.randint(300,600))
                    self.dir = random.randint(90, 180)
                case 6:
                    self.pos = (0-self.size,random.randint(0-self.size,300-self.size))
                    self.dir = random.randint(0, 90)
                case 7:
                    self.pos = (random.randint(0-self.size,300-self.size),0-self.size)
                    self.dir = random.randint(0, 90)

        else:
            self.pos = pos
            self.dir = rot
        
        # Sets the rect
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)

    # Updates the obstacle position and rotation
    def update(self):
        dir = math.radians(self.dir)
        # Increases the position by the direction
        self.pos = (self.pos[0] + math.sin(dir) * self.speed, self.pos[1] + math.cos(dir) * self.speed)

        # Updates the rects position
        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]
    
    def draw(self):
        # Draws the asteroid
        self.screen.blit(self.image, self.image.get_rect(center=self.rect.center))
        self.mask = pygame.mask.from_surface(self.image)
