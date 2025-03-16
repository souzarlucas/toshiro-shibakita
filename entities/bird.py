from components.position import Position
from components.sprite import Sprite
from components.velocity import Velocity
from components.score import Score
from components.collider import Collider
import pygame

class Bird:
    # Entidade que representa o pássaro no jogo.
    def __init__(self, x, y, image_path):
        self.position = Position(x, y)
        self.sprite = Sprite(image_path)
        self.velocity = Velocity(0, 0)
        self.score = Score()
        self.collider = Collider(pygame.Rect(x, y, self.sprite.image.get_width(), self.sprite.image.get_height()))

    def get_components(self):
        return [self.position, self.sprite, self.velocity, self.score, self.collider]

    def has_component(self, component_type):
        for component in self.get_components():
            if isinstance(component, component_type):
                return True
        return False

    def get_component(self, component_type):
        for component in self.get_components():
            if isinstance(component, component_type):
                return component
        return None