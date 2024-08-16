import tkinter as tk
from class_armario import Armario
from class_caixa import Caixa
from class_chave import Chave
from class_usuario import Usuario
from usuarios import *


def gerar_salas():
    salas = []
    sala = [100, 200, 300, 400]
    for s in sala:
        for x in range(5):
            salas.append(s)
            s += 1
    return salas


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle de Chaves")
        self.master.geometry("400x400")
        self.armario = Armario(gerar_salas())
        
        # Criando o main frame
        self.main_frame = tk.Frame(master)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configurando o tamanho da janela para expandir o frame
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        # Criando a listbox e configurando para preencher o frame
        self.listbox_usuarios = tk.Listbox(self.main_frame)
        self.listbox_usuarios.pack(fill="both", expand=True)
        # Criando um widget de texto para exibir a estante
       
      
       # Criando a barra de menus
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        # Criando o menu "Operações"
        operacoes_menu = tk.Menu(menubar, tearoff=0)
        operacoes_menu.add_command(label="Cadastrar Usuários", command=self.cadastrar_usuarios)
        operacoes_menu.add_command(label="Imprimir Usuários", command=self.imprimir_usuarios)
        operacoes_menu.add_separator()  # Cria uma linha separadora
        operacoes_menu.add_command(label="Visualizar Estante", command=self.visualizar_estante)
        # operacoes_menu.add_command(label="Pegar Caixa", command=self.pegar_caixa())
        operacoes_menu.add_command(label="Entregar Caixa", command=self.entregar_caixa)
        operacoes_menu.add_command(label="Localizar Caixa", command=self.localizar_caixa)
        menubar.add_cascade(label="Menu", menu=operacoes_menu)

    def cadastrar_usuarios(self):
        gerar_usuarios() # Chama a função para gerar os usuários
        # Limpa a listbox antes de preencher com novos dados
        self.listbox_usuarios.delete(0, tk.END)
        # Preenche a listbox com os nomes dos usuários
        for usuario in lista_usuarios:
            self.listbox_usuarios.insert(tk.END, f"{usuario.nome} - {usuario.matricula}")

    def imprimir_usuarios(self):
        # Limpa a listbox antes de preencher com novos dados
        self.listbox_usuarios.delete(0, tk.END)
        # Preenche a listbox com as informações dos usuários
        for usuario in lista_usuarios:
            self.listbox_usuarios.insert(tk.END, usuario.__str__())

    def visualizar_estante(self):
        for info in self.armario.get_prateleiras():
            self.listbox_usuarios.insert(tk.END, info)

    def pegar_caixa(self,master):
        # Obtém o usuário selecionado na Listbox
        usuario_selecionado = self.listbox_usuarios.get(tk.ACTIVE)

        # Cria uma janela modal para pedir o número da caixa
        janela_caixa = tk.Toplevel(self,master)
        janela_caixa.title("Digite o número da caixa")

        # Label e entrada para o número da caixa
        label_caixa = tk.Label(janela_caixa, text="Número da caixa:")
        label_caixa.pack()
        entry_caixa = tk.Entry(janela_caixa)
        entry_caixa.pack()

        # Botão para confirmar
        botao_confirmar = tk.Button(janela_caixa, text="Confirmar", command=lambda: self.confirmar_caixa(usuario_selecionado, entry_caixa.get(), janela_caixa))
        botao_confirmar.pack()

    def confirmar_caixa(self, usuario_selecionado, num_caixa, janela_caixa):
        # Chama a função para pegar a caixa
        self.armario.pegar_caixa_no_armario(usuario_selecionado, num_caixa)
        janela_caixa.destroy()  # Fecha a janela modal
        
        



 

    def entregar_caixa(self):
    # Implementar a lógica para entregar a caixa
        pass

    def localizar_caixa(self):
    # Implementar a lógica para localizar a caixa
        pass

    def fechar_programa(self):
        self.master.quit()


# Cria a janela principal
root = tk.Tk()
app = App(root)
root.mainloop()