import pygame  # Importa a biblioteca Pygame para manipulação de gráficos.

class Sprite:
    # Define a classe Sprite, que representa a imagem de uma entidade no jogo.
    def __init__(self, image_path):
        # Inicializa o sprite com o caminho da imagem.
        self.image = pygame.image.load(image_path)  # Carrega a imagem usando Pygame.
        self.rect = self.image.get_rect()  # Obtém o retângulo da imagem para detecção de colisões.

    def __repr__(self):
        # Define como a classe Sprite é representada como string.
        return f"Sprite(image_path='{self.image}')"