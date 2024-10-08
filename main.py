import pygame
import player
import enemies

pygame.init()

screen = pygame.display.set_mode((800,600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,255,0), pygame.Rect(390, 290, 20, 20))

    pygame.display.flip()

pygame.quit()