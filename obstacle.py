from dataclasses import dataclass
import pygame

@dataclass
class Asteroid:
    x: float
    y: float
    dirx: float
    diry: float
    sizex: int
    sizey: int
    speed: float
    screen: pygame.Surface

    def normalize(self):
        norm = (self.dirx**2 + self.diry**2)**0.5
        self.dirx /= norm
        self.diry /= norm

    def update(self, delta: float) -> None:
        self.x += self.dirx * self.speed * delta
        self.y += self.diry * self.speed * delta
    
    def draw(self) -> None:
        rect = pygame.Rect(self.x-self.sizex/2, self.y-self.sizey/2, self.sizex, self.sizey)
        pygame.draw.rect(self.screen, (0,255,0), rect)

class Enemy:
    def __init__(self) -> None:
        pass
