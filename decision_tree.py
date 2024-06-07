import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class DecisionTree:
    def __init__(self):
        self.G = nx.DiGraph()

    def carregar_dados(self):
        # Dados fictícios para calcular o ganho de informação
        data = {
            'Decisão A': [1, 0, 1, 0, 1],
            'Decisão B': [0, 1, 0, 1, 0],
            'Decisão C': [1, 1, 0, 0, 0],
            'Resultado': [1, 0, 1, 0, 1]
        }
        self.df = pd.DataFrame(data)

    # Função para calcular a entropia
    def entropy(self, p):
        return -p * np.log2(p) - (1 - p) * np.log2(1 - p) if p != 0 and p != 1 else 0

    def construir_arvore(self):
        # Calcular entropia do resultado atual
        p_positive = self.df['Resultado'].mean()
        current_entropy = self.entropy(p_positive)

        # Calcular o ganho de informação para cada decisão
        gains = {}
        gain = 0  # Inicializa a variável gain aqui
        for decision in ['Decisão A', 'Decisão B', 'Decisão C']:
            p_decision_true = self.df[decision].mean()
            entropy_decision_true = self.entropy(self.df[self.df[decision] == 1]['Resultado'].mean())
            entropy_decision_false = self.entropy(self.df[self.df[decision] == 0]['Resultado'].mean())
            avg_entropy_decision = p_decision_true * entropy_decision_true + (1 - p_decision_true) * entropy_decision_false
            gains[decision] = current_entropy - avg_entropy_decision
            gains[decision] = gain
            print(f"Ganho de informação para {decision}: {gain}")
       
        # Decidir a primeira decisão com base no maior ganho de informação
        primeira_decisao = max(gains, key=gains.get)

        # Adicionando os nós raiz
        self.G.add_node("Início")
        self.G.add_node(primeira_decisao)

        # Adicionando arestas com base na primeira decisão
        self.G.add_edge("Início", primeira_decisao, decision=primeira_decisao)

        print ("entropia", current_entropy)
        

        # Adicionando as outras decisões e folhas
        decisions = ['Decisão B', 'Decisão C']
        for decision in decisions:
            self.G.add_node(decision)
            self.G.add_node("Feliz após " + decision)
            self.G.add_node("Não feliz após " + decision)

            # Adicionando arestas para cada decisão
            self.G.add_edge(primeira_decisao, decision, decision=decision)
            self.G.add_edge(decision, "Feliz após " + decision, outcome="Feliz")
            self.G.add_edge(decision, "Não feliz após " + decision, outcome="Não feliz")

        # Adicionando as folhas para a primeira decisão
        self.G.add_node("Feliz após " + primeira_decisao)
        self.G.add_node("Não feliz após " + primeira_decisao)
        self.G.add_edge(primeira_decisao, "Feliz após " + primeira_decisao, decision=1)
        self.G.add_edge(primeira_decisao, "Não feliz após " + primeira_decisao, decision=0)

    def buscar_todas_as_folhas(self):
        # Função para buscar todas as folhas na árvore de decisão
        folhas = [no for no in self.G.nodes if self.G.out_degree(no) == 0]
        return folhas

    def buscar_proximo_no(self, no_atual, decisao):
        # Função para buscar o próximo nó na árvore de decisão
        filhos = list(self.G.successors(no_atual))
        if filhos:
            return filhos[decisao] if decisao < len(filhos) else None
        return None

    def entropy(self, p):
        # Função para calcular a entropia
        return -p * np.log2(p) - (1 - p) * np.log2(1 - p) if p != 0 and p != 1 else 0

    def desenhar_grafo(self):
        # Posicionamento dos nós para melhor visualização
        pos = {
            "Início": (0, 0),
            "Decisão A": (2, 0),
            "Feliz após Decisão A": (4, 0.5),
            "Não feliz após Decisão A": (4, -0.5),
            "Decisão B": (2, 1.5),
            "Feliz após Decisão B": (4, 2.5),
            "Não feliz após Decisão B": (4, 1),
            "Decisão C": (2, -1.5),
            "Feliz após Decisão C": (4, -1),
            "Não feliz após Decisão C": (4, -2.5)
        }

        # Desenhando o grafo
        plt.figure(figsize=(12, 8))
        nx.draw(self.G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrowsize=20)
        plt.show()
