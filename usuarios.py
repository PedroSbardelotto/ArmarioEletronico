from class_usuario import Usuario
from class_armario import Armario
from class_caixa import Caixa
from class_chave import Chave
import os
import json
lista_usuarios = []


def criar_armario():
    """
    Essa função tem como objetivo criar a intancia do objeto da classe Armario
    """
    armario = Armario(gerar_salas())
    return armario


def gerar_salas() -> list:
    """
    função que vai criar as salas de aulas numa lista
    Retorno:
    Retorna a lista de salas
    """
    salas = []
    sala = [100, 200, 300, 400]
    for s in sala:
        for x in range(2):
            salas.append(s)
            s += 1
    return salas


def gerar_usuarios() -> None:
    """
        Função que popula a lista de usuarios ao ser chamada.
        ela cria instancias da classe usuario.
    """
    aux_usuarios = ["João", "Christian", "Alfredo", "Gabriel", "Pedro", "Gui"]
    aux_matriculas = [1111, 2222, 3333, 4444, 5555, 6666]
    for ind in range(len(aux_usuarios)):
        adicionar_usuario(Usuario(aux_usuarios[ind], aux_matriculas[ind]))
        os.system("cls")


def adicionar_usuario(usuario) -> None:
    """
    função que adiciona as instancias do obj usuario na lista
    """
    lista_usuarios.append(usuario)


def imprimir_usuarios() -> str:
    """
    função que vai realizar a intereção dos atributos das intâncias, usando o metodo __str__.
    No meu sistema ela imprime o atributo "nome" do obj usuário e se o possui o atributo caixa da classe Caixa
    """
    os.system("cls")
    print("--- Usuários: ---")
    for usuario in lista_usuarios:
        print(f"---{usuario.__str__()}")


def escolher_usuario() -> list:
    """
    Essa função vai usar o enumerate para retornar os objetos da lista como objetos numerados
    No contexto de uso, podemos escolher qual usuário fará a próxima ação.
    """

    nomes_usuarios = [usuario.nome for usuario in lista_usuarios]
    return nomes_usuarios


def pegar_caixa_no_armario(armario: Armario, usuario_selecionado, num_caixa):
    """
    a função tem como objetivo chamar outra função encadenando uma série de ações
    que interagem com a classe Usuario, Caixa, Armario e seus respctivos métodos
    """
    os.system("cls")
    usuario_selecionado = escolher_usuario()
    caixa = armario.get_caixa(num_caixa)
    usuario_selecionado.retirar_caixa(caixa)


def filtrar_usuario_c_caixa(l_usuarios) -> list:
    # Filtrar usuarios com caixa e retornar uma lista
    lista_usuario_caixa = []  # lista de usuarios com caixa
    for usuario in l_usuarios:
        if usuario.tem_caixa():
            lista_usuario_caixa.append(usuario)
    return lista_usuario_caixa


def escolher_usuario_com_caixa(lista_usuario_caixa) -> Usuario:
    # Exibir usuario com caixa e permitir a escolha

    print("---Usuários com caixa---")
    for ind, usuario in enumerate(lista_usuario_caixa):
        print(f" {ind} - {usuario.nome} - Caixa: {usuario.caixa_retirada}.")

    return lista_usuario_caixa[int(input("Escolha: "))]


def devolver_caixa_para_armario(armario: Armario):  # devole a caixa para a posição original da prateleira
    os.system("cls")
    lista_usuario_caixa = filtrar_usuario_c_caixa(lista_usuarios)
    usuario_selecionado = escolher_usuario_com_caixa(lista_usuario_caixa)
    caixa = usuario_selecionado.recolocar_caixa()
    # armario = armario.receber_caixa(caixa, 10) #args
    armario = armario.receber_caixa(caixa=caixa)  # kwargs


def imprimir_prateleiras(armario):  # imprime as prateleiras
    os.system("cls")
    return armario.imprimir()


# Localizar caixa (com quem?)
def Localizar_caixa(usuario: Usuario, caixa_retirada: Caixa, l_usuarios=lista_usuarios):
    os.system("cls")
    num_caixa = int(input("Digite o N° da caixa: "))
    mensagem = None
    for usuario in l_usuarios:
        if usuario.caixa_retirada and usuario.caixa_retirada.numero == num_caixa:
            mensagem = print(
                f"Caixa -N° {num_caixa} está com o usuário {usuario.nome}")
            return mensagem
    if mensagem is None:
        print(f"Caixa N° {num_caixa} não está com nenhum usuário no momento.")


dict_usuarios = {}


def gerar_dict(dict_usuarios=dict_usuarios) -> dict:

    aux_usuarios = ["João", "Christian", "Alfredo", "Gabriel", "Pedro", "Gui"]
    # aux_matriculas = [1111, 2222, 3333, 4444, 5555, 6666]
    aux_matriculas = ["1111", "2222", "3333", "4444", "5555", "6666"]

    for ind in range(len(aux_usuarios)):
        usuario = Usuario(aux_usuarios[ind], aux_matriculas[ind])
        dict_usuarios[usuario.nome] = usuario.matricula
    return dict_usuarios


def write_json(dict_usuarios=dict_usuarios, filename='data_usuario.json', indent=4, separators=(',', ':\n')):
    """
    Escreve um dicionário de usuários em um arquivo JSON com formatação personalizada.

    Args:
        dict_usuarios: Dicionário contendo os dados dos usuários.
        filename: Nome do arquivo a ser criado (padrão: 'data_usuario.json').
        indent: Nível de indentação para formatar o JSON (padrão: 4).
        separators: Tupla com os separadores de itens e pares chave-valor (padrão: vírgula e nova linha).
    """
    dict_usuarios = gerar_dict()
    try:
        with open(filename, 'w') as file:
            json.dump(dict_usuarios, file, indent=indent,
                      separators=separators)
        print(f"Dados salvos em {filename}")
    except (IOError, TypeError) as e:
        print(f"Erro ao salvar o arquivo: {e}")


def read_json(filename='data_usuario.json'):
    """
    Lê um arquivo JSON e verifica se existem usuários.

    Args:
        filename: Nome do arquivo a ser lido (padrão: 'data_usuario.json').

    Returns:
        Um dicionário com os dados dos usuários, caso o arquivo exista e não esteja vazio.
        Caso contrário, retorna None.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if data:
                print("Já existem usuários no arquivo.")
                return data
            else:
                print("O arquivo está vazio.")
    except FileNotFoundError:
        print(f"O arquivo {filename} não foi encontrado.")
    except json.JSONDecodeError:
        print("O arquivo JSON está corrompido.")
    return None
