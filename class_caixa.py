from class_chave import Chave

class Caixa:
    def __init__(self, num_sala):
        self.__numero = num_sala
        self.__chave = Chave(num_sala)
        self.__caneta = None
        self.__ctrl_ar = None
        self.__ctrl_projetor = None

    def __str__(self):
        """
         Metodo que usa a função __str__ para retornar o objeto da classe como uma string.
         Retorna
        """
        return f"N°: [{self.__numero} - {self.__chave}]"


    @property
    def numero(self):
        """
        O decorador @property é utilizado para transformar o método em uma propriedade. Isso significa que você poderá acessar o valor do atributo numero como se fosse um atributo normal da classe, utilizando a sintaxe de ponto (objeto.numero).
        O decorador encapsula a lógica de acesso ao atributo privado, permitindo que você controle como o valor é obtido e formatado quando acessado externamente.
        """
        return self.__numero

  