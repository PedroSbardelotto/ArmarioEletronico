import random
class Chave:
    def __init__(self, num_sala):
        self.__numero = num_sala
        self.__segredo = str(random.randint(1000, 9000))

    def __str__(self):
        """
         Metodo que usa a função __str__ para retornar o objeto da classe como uma string.
         Retorna
        """
        return f"chave:<{self.__numero} - {self.__segredo}>"

