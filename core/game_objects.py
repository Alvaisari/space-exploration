import pygame

class CelestialObject:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image, window_width, window_height):
        # load image
        self.spaceship_image = pygame.image.load(image)
        self.spaceship_image = pygame.transform.scale(self.spaceship_image, (50, 50))

        # get dimensions of the image
        self.spaceship_rect = self.spaceship_image.get_rect()

        # set the initial position of the spaceship
        self.spaceship_rect.centerx = window_width // 2
        self.spaceship_rect.centery = window_height // 2

        # self.velocity

    
    def draw(self, window):
        window.blit(self.spaceship_image, self.spaceship_rect)


    def move(self, dx, dy):
        self.spaceship_rect.centerx += dx
        self.spaceship_rect.centery += dy
