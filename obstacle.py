import pygame
import random

class Asteroid:
    def __init__(self, speed, screen) -> None:
        size = random.randint(16,32)
        self.size = (size, size)
        self.speed = speed
        self.screen = screen
        self.pos = ()
        self.dir = ()

        spawn_pos = random.randint(0, 7)
        match spawn_pos:
            case 0:
                self.pos = (random.randint(300,600),0-size)
                self.dir = (random.uniform(-0.9,0.1),random.uniform(0.1,0.9))
            case 1:
                self.pos = (600,random.randint(0-size,300-size))
                self.dir = (random.uniform(-0.9,0.1),random.uniform(0.1,0.9))
            case 2:
                self.pos = (600,random.randint(300,600))
                self.dir = (random.uniform(-0.9,0.1),random.uniform(-0.9,0.1))
            case 3:
                self.pos = (random.randint(300,600),600)
                self.dir = (random.uniform(-0.9,0.1),random.uniform(-0.9,0.1))
            case 4:
                self.pos = (random.randint(0-size,300-size),600)
                self.dir = (random.uniform(0.1,0.9),random.uniform(-0.9,0.1))
            case 5:
                self.pos = (0-size,random.randint(300,600))
                self.dir = (random.uniform(0.1,0.9),random.uniform(-0.9,0.1))
            case 6:
                self.pos = (0-size,random.randint(0-size,300-size))
                self.dir = (random.uniform(0.1,0.9),random.uniform(0.1,0.9))
            case 7:
                self.pos = (random.randint(0-size,300-size),0-size)
                self.dir = (random.uniform(0.1,0.9),random.uniform(0.1,0.9))
        
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def normalize(self) -> None:
        norm = (self.dir[0]**2 + self.dir[1]**2)**0.5
        self.dir = (self.dir[0]/norm, self.dir[1]/norm)

    def update(self, delta: float) -> None:
        self.rect.left += self.dir[0] * self.speed * delta
        self.rect.top += self.dir[1] * self.speed * delta
    
    def draw(self) -> None:
        pygame.draw.rect(self.screen, (0,255,0), self.rect)

class Enemy:
    def __init__(self) -> None:
        pass
