import pygame
from components.position import Position
from components.collider import Collider

class Sky:
    # Entidade que representa o céu do jogo.
    def __init__(self, x, y, width, height):
        self.position = Position(x, y)
        self.collider = Collider(pygame.Rect(x, y, width, height))

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