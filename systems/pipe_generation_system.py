import random
import pygame
from components.position import Position
from components.collider import Collider
from components.sprite import Sprite
from entities.pipe import Pipe

class PipeGenerationSystem:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pipe_width = 50
        self.pipe_gap = 150
        self.pipe_speed = 5
        self.pipes = []
        self.pipe_top_image = pygame.image.load("assets/images/pipe_top.png")
        self.pipe_bottom_image = pygame.image.load("assets/images/pipe_bottom.png")

    def update(self, entities):
        # Gera novos canos aleatórios.
        if len(self.pipes) < 2:
            pipe_height = random.randint(100, self.screen_height - 300)
            pipe_top = pygame.Rect(self.screen_width, 0, self.pipe_width, pipe_height)
            pipe_bottom = pygame.Rect(self.screen_width, pipe_height + self.pipe_gap, self.pipe_width, self.screen_height - pipe_height - self.pipe_gap)
            self.pipes.append((pipe_top, pipe_bottom))

        # Move os canos para a esquerda.
        for pipe_top, pipe_bottom in self.pipes:
            pipe_top.x -= self.pipe_speed
            pipe_bottom.x -= self.pipe_speed

        # Remove os canos que saíram da tela.
        if self.pipes and self.pipes[0][0].right < 0:
            self.pipes.pop(0)

        # Adiciona os canos às entidades do jogo com imagens.
        for pipe_top, pipe_bottom in self.pipes:
            top_pipe = Pipe(pipe_top)
            top_pipe.sprite = Sprite("assets/images/pipe_top.png")
            entities.append(top_pipe)

            bottom_pipe = Pipe(pipe_bottom)
            bottom_pipe.sprite = Sprite("assets/images/pipe_bottom.png")
            entities.append(bottom_pipe)