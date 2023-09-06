import pygame
from random import randint
from core.game_objects import CelestialObject, Spaceship

pygame.init()

# constants
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
SPEED = 1
pygame.display.set_caption('Space Exploration Simulator')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# generate objects
spaceship = Spaceship('resources/spaceship.png', WIDTH, HEIGHT)

celestial_objects = []
for i in range(13):
    x = randint(0, WIDTH)
    y = randint(0, HEIGHT)
    size = randint(10, 50)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    celestial_objects.append(CelestialObject(x, y, size, color))

# build main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # handling spacecraft movement
    last_movement_time = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship.move(-SPEED, 0) 
    if keys[pygame.K_RIGHT]:
        spaceship.move(SPEED, 0)
    if keys[pygame.K_UP]:
        spaceship.move(0, -SPEED)
    if keys[pygame.K_DOWN]:
        spaceship.move(0, SPEED)

    current_time = pygame.time.get_ticks()
    if current_time - last_movement_time > 100:
        last_movement_time = current_time

    # clear the screen
    WINDOW.fill(BLACK)

    # draw objects
    spaceship.draw(WINDOW)

    for obj in celestial_objects:
        obj.draw(WINDOW)

    # update the display 
    pygame.display.update()

# quit pygame
pygame.quit()