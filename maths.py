import math

class Vector2:
    # un vecteur représente un point sur l'écran
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    # distance entre deux vecteurs
    @staticmethod
    def distance_between(vector_a, vector_b):
        return math.sqrt((vector_a.x - vector_b.x)**2 + (vector_a.y - vector_b.y)**2)
    
    # longueur d'un vecteur
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # augmente une vecteur
    def add(self, value):
        if isinstance(value, Vector2):
            self.x += value.x
            self.y += value.y
        else:
            self.x += value
            self.y += value

    # soustrais un vecteur
    def substract(self, value):
        if isinstance(value, Vector2):
            self.x -= value.x
            self.y -= value.y
        else:
            self.x -= value
            self.y -= value

    # multiplie un vecteur
    def multiply(self, value):
        if isinstance(value, Vector2):
            self.x *= value.x
            self.y *= value.y
        else:
            self.x *= value
            self.y *= value

    # divise un vecteur
    def divide(self, value):
        if isinstance(value, Vector2):
            self.x /= value.x
            self.y /= value.y
        else:
            self.x /= value
            self.y /= value
    
    # convertit un vecteur en un vecteur homogène
    def normalize(self):
        magnitude = self.length()
        if magnitude > 0:
            self.divide(magnitude)    