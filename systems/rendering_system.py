import pygame  # Importa a biblioteca Pygame.
from components.position import Position  # Importa a classe Position.
from components.sprite import Sprite  # Importa a classe Sprite.

class RenderingSystem:
    # Define a classe RenderingSystem, que desenha as entidades na tela.
    def __init__(self, screen):
        # Inicializa o sistema de renderização com a tela do jogo.
        self.screen = screen  # Armazena a tela do jogo.

    def update(self, entities):
        # Desenha todas as entidades na lista 'entities' na tela.
        for entity in entities:
            # Itera sobre todas as entidades.
            if entity.has_component(Position) and entity.has_component(Sprite):
                # Verifica se a entidade possui componentes Position e Sprite.
                position = entity.get_component(Position)  # Obtém o componente Position.
                sprite = entity.get_component(Sprite)  # Obtém o componente Sprite.
                sprite.rect.topleft = (position.x, position.y)  # Atualiza a posição do retângulo do sprite.
                self.screen.blit(sprite.image, sprite.rect)  # Desenha a imagem do sprite na tela.