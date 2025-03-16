from components.position import Position  # Importa a classe Position do módulo components.position.
from components.velocity import Velocity  # Importa a classe Velocity do módulo components.velocity.

class MovementSystem:
    # Define a classe MovementSystem, que atualiza a posição das entidades com base em sua velocidade.
    def update(self, entities, delta_time):
        # Atualiza a posição de todas as entidades na lista 'entities'.
        # 'delta_time' é o tempo decorrido desde o último quadro.
        for entity in entities:
            # Itera sobre todas as entidades.
            if entity.has_component(Position) and entity.has_component(Velocity):
                # Verifica se a entidade possui componentes Position e Velocity.
                position = entity.get_component(Position)  # Obtém o componente Position da entidade.
                velocity = entity.get_component(Velocity)  # Obtém o componente Velocity da entidade.
                position.x += velocity.x * delta_time  # Atualiza a coordenada x da posição.
                position.y += velocity.y * delta_time  # Atualiza a coordenada y da posição.