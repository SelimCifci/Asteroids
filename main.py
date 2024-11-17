import pygame
import obstacle

pygame.init()

screen = pygame.display.set_mode((600,600))

clock = pygame.time.Clock()
d = 0
frames = 0

frames_per_spawn = 60
obstacle_speed = 100

asteroids = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    frames += 1

    if frames_per_spawn >= 22 and frames % 300 == 0:
        frames_per_spawn -= 2
        obstacle_speed += 5

    if len(asteroids) < 24:
        if frames % frames_per_spawn == 0:
            asteroids.append(obstacle.Asteroid(obstacle_speed, screen))
            asteroids[len(asteroids)-1].normalize()
    else: asteroids.pop(0)

    for i in asteroids:
        i.update(d/1000)
        i.draw()

    pygame.display.flip()
    
    d = clock.tick(60)

pygame.quit()