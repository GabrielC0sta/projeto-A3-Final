import tkinter as tk
from decision_tree_gui import DecisionTreeGUI
from decision_tree import DecisionTree

def main():
    # Inicializa a interface gráfica
    root = tk.Tk()
    app = DecisionTreeGUI(root)
    
    # Carrega os dados e constrói a árvore de decisão
    tree = DecisionTree()
    tree.carregar_dados()
    tree.construir_arvore()
    
    # Plota a árvore de decisão
    tree.desenhar_grafo()
    
    root.mainloop()

if __name__ == "__main__":
    main()
