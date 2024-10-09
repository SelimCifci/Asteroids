import pygame
import player
import obstacle

pygame.init()

screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()
d=0

asteroid = obstacle.Asteroid(0,0,1,1,20,20,100,screen)
asteroid.normalize()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    asteroid.update(d/1000)
    asteroid.draw()

    pygame.display.flip()
    d = clock.tick(60)

pygame.quit()