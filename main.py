import pygame

pygame.init()

# constants
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Exploration Simulator')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# build main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear the screen
    WINDOW.fill(BLACK)

    # update the display 
    pygame.display.update()

# quit pygame
pygame.quit()