import pygame
from entities.bird import Bird
# ... (imports dos sistemas)

class Game:
    def __init__(self):
        # Inicializa a tela
        self.screen = pygame.display.set_mode((800, 600))  # Define o tamanho da tela
        pygame.display.set_caption("Toshiro Shibakita")  # Define o título da janela

        # Inicializa a fonte
        self.font = pygame.font.Font(None, 36)  # Cria a fonte para a pontuação

        # Inicializa o estado do jogo
        self.running = True  # Adiciona a variável running no construtor
        self.bird = Bird(100, 100, "assets/images/bird.png")  # Atualize o caminho para a imagem correta

    def run(self):
        # Loop principal do jogo
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # ... (eventos e delta_time)
            # ... (lógica do jogo)

            # Exibe a pontuação na tela
            score_text = self.font.render(f"Pontuação: {self.bird.score.value}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            # Atualiza a tela
            pygame.display.flip()