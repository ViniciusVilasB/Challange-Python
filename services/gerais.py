import sys
import os

def verifica_int(msg):
    '''
    Essa função obriga o usuário a digitar um número inteiro.
    Recebe uma mensagem para ser exibida ao usuário.
    '''

    num = input(msg)
    while not num.isnumeric():
        num = input(f'Digite apenas números: ')
    num = int(num)
    return num

def verifica_elemento(elem, lista):
    '''
    Esta função verifica se um determinado elemento existe na lista.
    Recebe o elemento e a lista como parâmetros.
    '''

    return elem in lista

def forca_opcao(msg, lista):
    '''
    Esta função força o usuário a digitar uma opção válida.
    Recebe uma mensagem a ser exibida e uma lista de opções válidas.
    '''

    opcao = verifica_int(msg)

    while not verifica_elemento(opcao, lista):
        print('Digite somente as opções válidas:', end=' ')
        print(*lista, sep=', ', end='.\n')
        opcao = verifica_int(msg)
    return opcao

def limpar_terminal():
    '''
    Essa função limpa o terminal caso esteja rodando em um ambiente padrão (Ex.: Windows, Linux ou macOS).
    '''

    if sys.stdin.isatty():
        os.system('cls') if os.name == 'nt' else os.system('clear')
        return True
    return False

def finalizar_app():
    '''
    Essa função finaliza a aplicação.
    '''

    limpar_terminal()
    exibicao_personalizada('Programa Encerrado')
    sys.exit()

def titulo(esta_na_main=False):
    '''
    Essa função exibe o título da página.
    Recebe um parâmetro opcional para verificar se está na função main.
    '''

    if limpar_terminal() or esta_na_main:
        print(''' 
███████╗      ███╗   ███╗ █████╗ ████████╗██╗ █████╗ ███╗  ██╗
██╔════╝      ████╗ ████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗ ██║
█████╗  █████╗██╔████╔██║██║  ██║   ██║   ██║██║  ██║██╔██╗██║
██╔══╝  ╚════╝██║╚██╔╝██║██║  ██║   ██║   ██║██║  ██║██║╚████║
███████╗      ██║ ╚═╝ ██║╚█████╔╝   ██║   ██║╚█████╔╝██║ ╚███║
╚══════╝      ╚═╝     ╚═╝ ╚════╝    ╚═╝   ╚═╝ ╚════╝ ╚═╝  ╚══╝
                        - 🅶🆁🅸🅳 - 
''')

def exibicao_personalizada(titulo, msg=None):
    print('\n' + "=" * 60)
    print(f'{titulo:^60}')
    print('=' * 60)

    if msg:
        print(msg)
        print('=' * 60)