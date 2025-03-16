import pygame
from core.game import Game

if __name__ == "__main__":
    pygame.init()  # Inicializa todos os módulos do pygame
    game = Game()
    game.run()
    pygame.quit()  # Encerra todos os módulos do git branch