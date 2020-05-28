from enum import IntEnum

class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    SKY_BLUE = (41, 173, 255)
    GRASS_GREEN = (0, 168, 68)
    OCEAN_BLUE = (60, 188, 252)
    DARK_BLUE = (0, 64, 88)
    WOOD_BROWN = (172, 124, 0)
    GRAY = (120, 120, 120)
    LIGHT_GRAY = (188, 188, 188)
    LIGHT_BLUE = (104, 136, 252)
    LIGHT_PINK = (248, 164, 192)
    TEAL = (0, 136, 136)

class Window:
    WIDTH = 640
    HEIGHT = 480
    FPS = 60

class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    NONE = 4