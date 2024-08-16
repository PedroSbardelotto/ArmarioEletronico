from class_caixa import Caixa


class Armario:
    def __init__(self, salas):
        self.__prateleira = {}
        for sala in salas:
            self.__prateleira[sala] = Caixa(sala)

    def imprimir(self):
        """
        O Metodo imprimir tem como objetivo mostrar uma representação textual do armário e suas prateleiras com suas caixas e chaves.
        Se houver algum espaço vazio ele será mostrado durante a impressão
        """

        print("               Prateleiras:")
        print("           N° prateleira = N° caixa")
        print(" ")
        for num_prateleira, caixa in self.__prateleira.items():
            if caixa is None:
                print("Prateleira: N°: SLOT SEM CAIXA")
            else:
                print(f"Prateleira: N°:{num_prateleira}| {caixa}")

    def is_vazia(self, num_prateleira: int) -> bool:
        """
        Verifica se a prateleira especificada está vazia.

        Args:
            num_prateleira (int): Número da prateleira a ser verificada.

        Returns:
            bool: True se a prateleira estiver vazia, False se estiver ocupada.
        """
        try:
            caixa = self.__prateleira[num_prateleira]
            return not caixa
        except KeyError:
            return True
    
    def get_prateleiras(self):
        prateleira_info = []
        for num, caixa in self.__prateleira.items():
            prateleira_info.append(f"Prateleira {num}: {caixa}")
        return prateleira_info  # Returning a list of strings
    
    def get_caixa(self, num_prateleira: int) -> Caixa:
        """
        Remove a caixa da prateleira especificada, se a prateleira estiver vazia.

        Args:
        num_prateleira (int): Número da prateleira a ser verificada.

        Returns:
        Caixa: Objeto Caixa se a prateleira estiver vazia, None caso contrário.
        """
        if self.is_vazia(num_prateleira):
            print(f"A prateleira {num_prateleira} está vazia. Sem caixa para retirar")
            return None

        else:
            caixa = self.__prateleira[num_prateleira]
            self.__prateleira[num_prateleira] = None
            return caixa

    def receber_caixa(self, caixa: Caixa) -> bool:

        # if not self.is_vazia(num_prateleira):
        #     print(f"A prateleira {num_prateleira} já está ocupada.")
        #     return False
        num_prateleira = caixa.numero
        self.__prateleira[num_prateleira] = caixa
