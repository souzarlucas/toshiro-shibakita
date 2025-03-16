from components.position import Position
from components.score import Score

class ScoreSystem:
    # Sistema que atualiza a pontuação do jogo.
    def update(self, entities):
        bird = None
        pipes = []
        # Separa o pássaro e os canos.
        for entity in entities:
            if isinstance(entity, Bird):
                bird = entity
            elif entity.has_component(Position):
                pipes.append(entity)

        if bird and bird.has_component(Score):
            bird_score = bird.get_component(Score)
            # Verifica se o pássaro passou por um cano.
            for pipe in pipes:
                pipe_position = pipe.get_component(Position)
                if pipe_position.x + pipe_position.width < bird.position.x and not pipe.passed:
                    bird_score.value += 1
                    pipe.passed = True # Marca o cano como passado.