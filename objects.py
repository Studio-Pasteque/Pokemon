import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, path_to_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path_to_image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.location = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.bounds = pygame.Rect(x, y, self.width, self.height)
    
    def update(self):
        self.velocity = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x -= 4
        if keys[pygame.K_RIGHT]:
            self.velocity.x += 4
        if keys[pygame.K_UP]:
            self.velocity.y -= 4
        if keys[pygame.K_DOWN]:
            self.velocity.y += 4
        
        self.location += self.velocity
        self.bounds = pygame.Rect(self.location.x, self.location.y, self.width, self.height)
    
    def set_width(self, width):
        self.width = width
        self.bounds = pygame.Rect(self.location.x, self.location.y, self.width, self.height)
    
    def set_height(self, height):
        self.height = height
        self.bounds = pygame.Rect(self.location.x, self.location.y, self.width, self.height)
    
    def set_location(self, x, y):
        self.location = pygame.math.Vector2(x, y)
        self.bounds = pygame.Rect(self.location.x, self.location.y, self.width, self.height)