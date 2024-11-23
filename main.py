import pygame
import obstacle
import player
import math

# Initialize the pygame modules
pygame.init()
pygame.font.init()

# Create a windows with the size 600,600
screen = pygame.display.set_mode((600,600))

# Set a font
font = pygame.font.SysFont('arial', 30)

# Instatantiate a pygame clock to stabilize FPS
clock = pygame.time.Clock()
# Variable to keep track of the frames 
frames = 0
# Variable to store the player inputs for WASD (x=1 -> a, x=-1 -> d, x=0 -> !a and !d)
inputs = [0,0]

# Frames that have to pass until a new asteroid spawns
frames_per_spawn = 60
# Speed of the asteroids
obstacle_speed = 1

# List that stores all asteroids
asteroids = []
# Instantiate the player
player1 = player.Player((24,32), 3.5, 5, screen, 30)

running = True
while running:
    # Checks if the window gets closed
    for event in pygame.event.get():
        # If true quits the while loop and program gets closed
        if event.type == pygame.QUIT:
            running = False

    # Fills the windows with a background color. In this case black
    screen.fill((0,0,0))

    # Checks if the amount the game gets harder crosses a limit and if 3 seconds passed (FPS is locked to 60 | 3*60 = 180)
    if frames_per_spawn >= 20 and frames % 180 == 0:
        # Lowers the frames per spawn, so that more asteroids spawn in a shorter peroid of time
        frames_per_spawn -= 4
        # Increases the speed of the asteroids
        obstacle_speed += 0.1

    # If the frames per spawn passed, spawns a new asteroid
    if frames % frames_per_spawn == 0:
        asteroids.append(obstacle.Asteroid(obstacle_speed, screen))
        # If the amount of asteroids exceeds a limit of 64 removes the first one to counter stuttering
        if len(asteroids) > 64:
            asteroids.pop(0) 

    for i in asteroids:
        # Updates and draws every asteroid
        i.update()
        i.draw()

        for j in player1.bullets:
            # Checks if any bullet and any asteroid collide with eachother trough pygame.mask.overlap()
            if j.mask.overlap(i.mask, (i.pos[0]-j.pos[0], i.pos[1]-j.pos[1])):
                # Delete the asteroid and the bullet
                asteroids.remove(i)
                player1.bullets.remove(j)

        # Checks if any asteroid collides with the player
        if player1.mask.overlap(i.mask, (i.pos[0]-player1.pos[0], i.pos[1]-player1.pos[1])):
            # Closes the program
            running = False

    # Checks if the cooldown for the player being able to shoot again ended
    player1.cooldown(frames)

    # pygame.key.get_pressed() returns a list containing all keys as bools (key pressed -> true, key released -> false)
    key = pygame.key.get_pressed()
    # Changes the input variable to the values of the pressed keys (see line 20)
    if key[pygame.K_w]: inputs[0] = 1
    elif key[pygame.K_s]: inputs[0] = -1
    else: inputs[0] = 0
    if key[pygame.K_d]: inputs[1] = -1
    elif key[pygame.K_a]: inputs[1] = 1
    else: inputs[1] = 0
    # If the space key is pressed, the player shoots
    if key[pygame.K_SPACE]: player1.shoot(frames)

    # Updates and draws the player
    player1.update(inputs)
    player1.draw()

    # Displays the score on the top left corner (1 sec = 6 points)
    screen.blit(font.render("Score: "+str(math.floor(frames/10)), False, (255,255,255)), (8,4))

    # Updates the whole window
    pygame.display.flip()
    
    # Locks the FPS to 60
    clock.tick(60)
    # Updates the frames passed since start
    frames += 1

# Closes the window
pygame.quit()