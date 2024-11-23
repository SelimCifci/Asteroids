import pygame
import math

class Player:
    def __init__(self, size, speed, rot_speed, screen, shoot_cooldown) -> None:
        self.size = size
        self.speed = speed
        self.rot_speed = rot_speed
        self.screen = screen
        self.shoot_cooldown = shoot_cooldown
        
        self.pos = (300-size[0]/2, 300-size[1]/2)
        self.dir = ()
        self.rot = 0
        self.bullets = []
        self.can_shoot = True
        self.shot_at = 0

        self.rect = pygame.Rect
        self.rot_rect = pygame.Rect

        self.image = pygame.image.load("player.png")
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

    def update(self, inputs):
        self.rot += inputs[1] * self.rot_speed
        self.dir = (math.cos(math.radians(self.rot)), -math.sin(math.radians(self.rot)))

        norm = (self.dir[0]**2 + self.dir[1]**2)**0.5
        if self.dir[0] != 0 and self.dir[1] != 0: self.dir = (self.dir[0]/norm, self.dir[1]/norm)
        self.pos = (self.pos[0] + self.dir[0] * self.speed * inputs[0], self.pos[1] + self.dir[1] * self.speed * inputs[0])

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        for i in self.bullets:
            if -6 < i.rect.left < 606 and -6 < i.rect.top < 606:
                i.update()
            else:
                self.bullets.remove(i)

    def shoot(self, time):
        if self.can_shoot:
            self.bullets.append(Bullet(self.screen, 8, 8, (self.rect.center[0]-3, self.rect.center[1]-3), self.dir))
            self.can_shoot = False
            self.shot_at = time

    def cooldown(self, time):
        if time >= self.shot_at+self.shoot_cooldown:
            self.can_shoot = True

    def draw(self):
        for i in self.bullets:
            i.draw()

        image = pygame.transform.rotate(self.image, self.rot-90)
        self.screen.blit(image, image.get_rect(center=self.rect.center))

class Bullet:
    def __init__(self, screen, size, speed, pos, dir) -> None:
        self.screen = screen
        self.size = size
        self.speed = speed
        self.pos = pos
        self.dir = dir

        self.rect = pygame.Rect(self.pos[0], self.pos[1], size, size)

        self.image = pygame.image.load("bullet.png")
        
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed, self.pos[1] + self.dir[1] * self.speed)

        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]

    def draw(self):
        self.screen.blit(self.image, self.image.get_rect(center=self.rect.center))
