import pygame

class Collider:
    # Componente que define um retângulo de colisão para a entidade.
    def __init__(self, rect):
        self.rect = rect # Armazena o retângulo de colisão.

    def __repr__(self):
        return f"Collider(rect={self.rect})"