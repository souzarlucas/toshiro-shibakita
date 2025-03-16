class Velocity:
    # Define a classe Velocity, que representa a velocidade de uma entidade no jogo.
    def __init__(self, x, y):
        # Inicializa a velocidade com as componentes x e y.
        self.x = x  # Armazena a componente x da velocidade.
        self.y = y  # Armazena a componente y da velocidade.

    def __repr__(self):
        # Define como a classe Velocity é representada como string.
        return f"Velocity(x={self.x}, y={self.y})"