import pygame
import math

class Player:
    def __init__(self, size, speed, rot_speed, screen, shoot_cooldown) -> None:
        self.size = size
        self.speed = speed
        self.rot_speed = rot_speed
        self.screen = screen
        self.shoot_cooldown = shoot_cooldown
        
        # Sets position to the center of the screen minus half the players size
        self.pos = (300-size[0]/2, 300-size[1]/2)
        self.dir = ()
        # Rotation of the player stored in degrees
        self.rot = 0
        # Stores the already shot bullets
        self.bullets = []
        self.shot_at = 0

        # Creates a rect for the player
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        # Creates a rect for the rotated image
        self.rot_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        # Stores the player graphic as a pygame.surface
        self.image = pygame.image.load("player.png")
        # Creates a pygame.mask for better collision detection
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

    # Updates the player
    def update(self, inputs):
        # Increases the rotation by the player inputs times the rot_speed
        self.rot += inputs[1] * self.rot_speed
        # Converts self.rot into a 2D vector using math.sin and cos
        self.dir = (math.cos(math.radians(self.rot)), -math.sin(math.radians(self.rot)))

        # Increases the position by the direction times speed
        self.pos = (self.pos[0] + self.dir[0] * self.speed * inputs[0], self.pos[1] + self.dir[1] * self.speed * inputs[0])

        # Updates the rects position
        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]

        # Checks for every bullet, if it's out of the screen
        for i in self.bullets:
            if -6 < i.rect.left < 606 and -6 < i.rect.top < 606:
                # If it's in the screen, updates it's position
                i.update()
            else:
                # If not removes it
                self.bullets.remove(i)

    def shoot(self, time):
        # Checks if the cooldown passed
        if time >= self.shot_at+self.shoot_cooldown:
            # If so, instantiates a new bullet
            self.bullets.append(Bullet(self.screen, 4, 8, (self.rect.center[0]-3, self.rect.center[1]-3), self.dir))
            # Starts the cooldown
            self.shot_at = time

    def draw(self):
        # Draws every bullet
        for i in self.bullets:
            i.draw()

        # Rotates the player graphic
        image = pygame.transform.rotate(self.image, self.rot-90)
        # Updates the new mask
        self.mask = pygame.mask.from_surface(image.convert_alpha())
        # Draws the player
        self.screen.blit(image, image.get_rect(center=self.rect.center))

class Bullet:
    def __init__(self, screen, size, speed, pos, dir) -> None:
        self.screen = screen
        self.size = size
        self.speed = speed
        self.pos = pos
        self.dir = dir

        # Creates a rect
        self.rect = pygame.Rect(self.pos[0], self.pos[1], size, size)
        
        # Stores the bullet graphic
        self.image = pygame.image.load("bullet.png")
        # Creates a pygame.mask
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

    # Uodates the position of the bullet
    def update(self):
        # Increases the position by the direction times speed
        self.pos = (self.pos[0] + self.dir[0] * self.speed, self.pos[1] + self.dir[1] * self.speed)

        # Updates the rects position
        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]

    def draw(self):
        # Draws the bullet
        self.screen.blit(self.image, self.image.get_rect(center=self.rect.center))
