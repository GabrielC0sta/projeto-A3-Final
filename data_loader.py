import pandas as pd

class DataLoader:
    @staticmethod
    def carregar_dados():
        # Dados fictícios para calcular o ganho de informação
        data = {
            'Decisão A': [1, 0, 1, 0, 1],
            'Decisão B': [0, 1, 0, 1, 0],
            'Decisão C': [1, 1, 0, 0, 0],
            'Resultado': [1, 0, 1, 0, 1]
        }
        df = pd.DataFrame(data)
        return df