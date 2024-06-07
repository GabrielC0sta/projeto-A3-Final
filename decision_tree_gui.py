import tkinter as tk
from tkinter import ttk, messagebox
from decision_tree import DecisionTree


class DecisionTreeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Árvore de Decisão")

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12), padding=10)
        self.style.configure("TEntry", font=("Arial", 12))

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        self.label_atual = ttk.Label(self.frame, text="Nó Atual: Início")
        self.label_atual.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        ttk.Label(self.frame, text="Decisão (1 ou 0):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_decisao = ttk.Entry(self.frame)
        self.entry_decisao.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.frame, text='Buscar', command=self.buscar_resultado).grid(row=2, column=0, pady=10, sticky=tk.W)
        ttk.Button(self.frame, text='Resetar', command=self.resetar_busca).grid(row=2, column=1, pady=10, sticky=tk.E)

        self.tree = DecisionTree()
        self.tree.carregar_dados()
        self.tree.construir_arvore()
        self.no_atual = "Início"
        self.folhas = self.tree.buscar_todas_as_folhas()

    def buscar_resultado(self):
        try:
            entrada_decisao = self.entry_decisao.get()
            if not entrada_decisao:
                messagebox.showerror("Erro", "Por favor, insira um valor para a decisão.")
                return
            decisao = int(entrada_decisao)
            if decisao not in [0, 1]:
                raise ValueError
            proximo_no = self.tree.buscar_proximo_no(self.no_atual, decisao)
            if proximo_no:
                self.no_atual = proximo_no
                if self.no_atual in self.folhas:
                    messagebox.showinfo("Resultado", f"Resultado final: {self.no_atual}")
                else:
                    self.label_atual.config(text=f"Nó Atual: {self.no_atual}")
            else:
                messagebox.showerror("Erro", "Caminho inválido na árvore.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido (1 ou 0) para a decisão.")
        except IndexError:
            messagebox.showerror("Erro", "Caminho inválido na árvore.")

    def resetar_busca(self):
        self.no_atual = "Início"
        self.label_atual.config(text=f"Nó Atual: {self.no_atual}")
