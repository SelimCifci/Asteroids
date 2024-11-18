import pygame
import obstacle
import player


pygame.init()

screen = pygame.display.set_mode((600,600))

clock = pygame.time.Clock()
d = 0
frames = 0
inputs = [0,0]

frames_per_spawn = 60
obstacle_speed = 100

asteroids = []
player1 = player.Player((24,24), 3.5, 5, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    frames += 1

    if frames_per_spawn >= 12 and frames % 300 == 0:
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

        for j in player1.bullets:
            if pygame.Rect.colliderect(j.rect, i.rect):
                asteroids.remove(i)
                break

        if pygame.Rect.colliderect(i.rect, player1.rect):
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]: inputs[0] = 1
    elif key[pygame.K_s]: inputs[0] = -0.5
    else: inputs[0] = 0
    if key[pygame.K_d]: inputs[1] = -1
    elif key[pygame.K_a]: inputs[1] = 1
    else: inputs[1] = 0
    if key[pygame.K_SPACE]: player1.shoot()

    player1.transform(inputs)
    player1.draw()

    pygame.display.flip()
    
    d = clock.tick(60)

pygame.quit()