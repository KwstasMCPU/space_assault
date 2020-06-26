import pygame

BLACK = (0,0,0)

class Hero(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()


        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the spaceship
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
		# Check if the paddles are off the edge of the screen (y-axis)
        if self.rect.y < 590:
            self.rect.y = 590

    def moveDown(self, pixels):
        self.rect.y += pixels
        # Check if the paddles are off the edge of the screen (y-axis)
        if self.rect.y > 740:
            self.rect.y = 740

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 8:
            self.rect.x = 8
    
    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 670:
            self.rect.x = 670