import pygame

BLACK = (0,0,0)

class Hero(pygame.sprite.Sprite):
    def __init__(self, color, height, width, health):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the spaceship
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.health = health

    def moveUp(self, pixels):
        self.rect.y -= pixels
		# Check if the Hero(spacehip) is off the edge of the screen (y-axis)
        if self.rect.y < 590:
            self.rect.y = 590

    def moveDown(self, pixels):
        self.rect.y += pixels
        # Check if the Hero is off the edge of the screen (y-axis)
        if self.rect.y > 730:
            self.rect.y = 730

    def moveLeft(self, pixels):
        # Check if the Hero is off the edge of the screen (y-axis)
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # Check if the Hero is off the edge of the screen (y-axis)
        if self.rect.x > 690:
            self.rect.x = 690
