class Score:
    # Componente que armazena a pontuação da entidade.
    def __init__(self, value=0):
        self.value = value # Armazena o valor da pontuação.

    def __repr__(self):
        return f"Score(value={self.value})"