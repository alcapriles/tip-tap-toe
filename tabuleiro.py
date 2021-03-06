import tkinter as tk
from tkinter import messagebox
import numpy as np
from jogo import Jogo

class Tabuleiro:
    def __init__(self):
        # Definindo janela
        self.window = tk.Tk()
        self.window.title("Jogo da velha!")
        self.window.geometry("300x350+100+100")
        self.window.rowconfigure(0, minsize=50)
        self.window.rowconfigure(1, minsize=100)
        self.window.rowconfigure(2, minsize=100)
        self.window.rowconfigure(3, minsize=100)
        self.window.columnconfigure(0, minsize=100)
        self.window.columnconfigure(1, minsize=100)
        self.window.columnconfigure(2, minsize=100)
        
        # definindo botôes
        for i in range(1,4):
            for j in range(3):
                self._fazer_botao(i,j)

        self.label = tk.Label(self.window)
        self.label.grid(row = 0, column = 0, columnspan=3)
        self.label.configure(font="Courier 20 bold")
        self.label.configure(text = "Jogo da Velha")   

        # criando o jogo
        self.jogo = Jogo()

    def _fazer_botao(self, linha, coluna):
        botao = tk.Button(self.window)
        botao.configure(command = lambda i=linha, j=coluna: self.botao_clicado(i, j, botao))
        botao.grid(row=linha, column=coluna, sticky="nsew")

    def iniciar(self):
        self.window.mainloop() 

    def botao_clicado(self, i, j, botao):
        print('Botão {0}, {1} clicado'.format(i-1, j))
        botao.configure(font="Courier 35 bold")
        botao.configure(text = self.jogo.jogador)
        botao.configure(state = "disabled")
        self.jogo.recebe_jogada(i-1, j)
        status = self.jogo.verifica_ganhador()
        if status == 1 or status == 2:
            resultado = messagebox.showinfo(title="Resultado", message=('E o ganhador é... X!') if status == 1 else 'E o ganhador é... O!')
            resultado = messagebox.askyesno(title= "Resultado", message= "Deu velha! Iniciar novo jogo?")
            messagebox.showinfo(title="Novo jogo", message="Tem certeza?")
            self.jogo.limpa_jogadas()
            if resultado == True:
                for i in range(1,4):
                    for j in range(3):
                        self._fazer_botao(i,j)
        elif status == 0:
            resultado = messagebox.askyesno(title= "Resultado", message= "Deu velha! Iniciar novo jogo?")
            messagebox.showinfo(title="Novo jogo?", message="Tem certeza?")
            self.jogo.limpa_jogadas()
            if resultado == True:
                for i in range(1,4):
                    for j in range(3):
                        self._fazer_botao(i,j)
                        
                        
                         
            
j = Tabuleiro()
j.iniciar()