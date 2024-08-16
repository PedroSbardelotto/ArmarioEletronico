
from class_armario import *


class Usuario:
    def __init__(self, nome: str, matricula: str, telefone=None, ender=None) -> None:
        self.__nome = nome  # string
        self.__telefone = telefone
        self.__endereco = ender
        self.__matricula = matricula  # string
        self.__caixa_retirada = None  # instancia Caixa

    """
    O decorador @property é utilizado para transformar o método em uma propriedade. Isso significa que você poderá acessar o valor do atributo numero como se fosse um atributo normal da classe, utilizando a sintaxe de ponto (objeto.numero).
    O decorador encapsula a lógica de acesso ao atributo privado, permitindo que você controle como o valor é obtido e formatado quando acessado externamente.
    """
    @property
    def matricula(self) -> str:
        return self.__matricula

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def caixa_retirada(self) -> Caixa:
        return self.__caixa_retirada

    @nome.setter
    def nome_setter(self, novo_nome) -> nome:
        self.__nome = novo_nome

    def retirar_caixa(self, caixa: Caixa) -> Caixa:
        """
        Função que permite que um usuário retire uma caixa de um armário.
        """
        self.__caixa_retirada = caixa
        return caixa

    def recolocar_caixa(self) -> Caixa:
        caixa = self.__caixa_retirada
        self.__caixa_retirada = None
        return caixa

    def tem_caixa(self):
        """
        O metodo verifica se o usuário tem uma caixa.
        Retorna true se tem, false se não tiver
        """
        return self.__caixa_retirada is not None

    def __str__(self) -> str:
        """
         Metodo que usa a função __str__ para retornar o objeto da classe como uma string.
         Retorna
        """
        if self.__caixa_retirada:
            return f" {self.__nome} está com a chave {self.__caixa_retirada.numero}."
        return f" {self.__nome} não está com nenhuma chave."


"""
Abaixo estão as classes filhas que vão herdar metodos e atributos da classe pai Usuario
Essas subclasses não vão ser usadas no programa principal. 
"""


lst_setores = ['Manutenção', 'Secretaria', 'TI', 'Eventos', 'Limpeza']


class Funcionario(Usuario):
    def __init__(self, nome, matricula, setor=lst_setores[2]):
        super().__init__(nome, matricula)
        self.__setor = setor

    def __str__(self):
        return f"""{self.nome}- {self.__setor}"""


lst_disciplinas = ['Lógica de Programação', 'POO', 'BD', 'Redes']


class Professor(Funcionario):
    def __init__(self, nome, matricula, setor=lst_setores[1], disciplina="None", turno=None):
        super().__init__(nome, matricula, setor)
        self.__turno = turno
        self.__disciplina = disciplina


lst_motivos = ['Manutenção', 'Instalação',
               'Configuração', 'Troca de Equipamentos']


class TI(Usuario):
    def __init__(self, nome, matricula=None, motivo=None):
        super().__init__(nome, matricula)
        self.__motivo = motivo


# TESTES
"""
Os testes de criação de instancias de subclasses.
hardcoded para ficar mais facíl a compreensão do que esta sendo feito. 


usuarios = [Professor("Ana", "11121"), Funcionario("Maria", "y75675"), Professor("Juca", "u65576"), Usuario("Duda", "8787")]

for obj in usuarios:
     print(f" Nome: {obj.nome}.") # Fazendo o print do atributo nome de cada uma das instancias 

"""
# teste = Usuario("pedro","000192923")

# print(teste)
