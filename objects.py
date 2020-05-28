from utilities import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, path_to_image):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load(path_to_image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.location = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.bounds = pygame.Rect(x, y, self.width, self.height)
        self.direction = Direction.DOWN
    
    def update(self):
        self.velocity = pygame.math.Vector2(0, 0)
        
        if self.direction == Direction.LEFT:
            self.velocity.x -= 2
        if self.direction == Direction.RIGHT:
            self.velocity.x += 2
        if self.direction == Direction.UP:
            self.velocity.y -= 2
        if self.direction == Direction.DOWN:
            self.velocity.y += 2
        if self.direction == Direction.NONE:
            self.velocity = pygame.math.Vector2(0, 0)
            
        self.move()
        
        self.location += self.velocity
        self.bounds = pygame.Rect(self.location.x, self.location.y, self.width, self.height)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            self.direction = Direction.RIGHT
        elif keys[pygame.K_UP]:
            self.direction = Direction.UP
        elif keys[pygame.K_DOWN]:
            self.direction = Direction.DOWN
        else:
            self.direction = Direction.NONE
    
    def set_width(self, width):
        self.width = width
        self.bounds = pygame.Rect(self.location.x, self.location.y, self.width, self.height)
    
    def set_height(self, height):
        self.height = height
        self.bounds = pygame.Rect(self.location.x, self.location.y, self.width, self.height)
    
    def set_location(self, x, y):
        self.location = pygame.math.Vector2(x, y)
        self.bounds = pygame.Rect(self.location.x, self.location.y, self.width, self.height)
    
    def collide_with(self, rect):
        if self.bounds.colliderect(rect):
            print("collision")
        else:
            print("")

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, path_to_image):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load(path_to_image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.location = pygame.math.Vector2(x, y)
        self.bounds = pygame.Rect(x, y, self.width, self.height)
    
    def update(self):
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
    
    def collide_with(self, rect):
        if self.bounds.colliderect(rect):
            print("collision")
        else:
            print("")