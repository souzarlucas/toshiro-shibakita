class Position:
    # Define a classe Position, que representa a posição de uma entidade no jogo.
    def __init__(self, x, y):
        # Inicializa a posição com as coordenadas x e y.
        self.x = x  # Armazena a coordenada x.
        self.y = y  # Armazena a coordenada y.

    def __repr__(self):
        # Define como a classe Position é representada como string.
        # Isso é útil para depuração e exibição de informações.
        return f"Position(x={self.x}, y={self.y})"