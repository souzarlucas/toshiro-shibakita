import pygame
from components.position import Position
from components.collider import Collider

class Pipe:
    # Entidade que representa um cano no jogo.
    def __init__(self, rect):
        self.position = Position(rect.x, rect.y)
        self.collider = Collider(rect)
        self.passed = False # Indica se o pássaro já passou pelo cano.

    def get_components(self):
        return [self.position, self.collider]

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