import os
import sys

from usuarios import lista_usuarios
from cadastro import cadastrar
from login import entrar
from corridas import proxima_corrida

'''
import logging

# Configurando o logger para diferentes níveis de log
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Exemplo de diferentes níveis de log
logging.debug('Isso é uma mensagem de depuração')
logging.info('Isso é uma mensagem informativa')
logging.warning('Isso é um alerta')
logging.error('Ocorreu um erro!')
logging.critical('Erro crítico! O sistema pode parar de funcionar.')
'''

lista_equipes = ["ABT Cupra", "Andretti", "DS Penske", "Envision", "ERT", "Jaguar TCS",
                 "Mahindra", "Maseratti MSG", "Mclaren", "Nissan", "Tag Heuer Porsche", "Nenhuma"]

##############################################################################################################

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

def alterar_equipe(retornar_para):
    texto = ''
    for i in range(len(lista_equipes) - 1):
        if i % 2 == 0:
            if lista_equipes[i] != lista_equipes[-2]:
                texto += f'{i + 1}. {lista_equipes[i]:<30}\t{i + 2}. {lista_equipes[i + 1]}\n'
            else:
                texto += f'{i + 1}. {lista_equipes[i]:<30}\t{i + 2}. {lista_equipes[i + 1]}'

    exibicao_personalizada('Altere a equipe', texto)
    '''
    print(f'{'1. Alterar equipe favorita':<30}\t2. Voltar\n'
          f'{'=' * 60}')
    '''
    print(f'Favorita atual: {usuario['equipe_favorita']}')
    opcao_escolhida = forca_opcao('\nEscolha uma nova equipe para acompanhar: ', range(1, 13))

    usuario['equipe_favorita'] = lista_equipes[opcao_escolhida - 1]

    return retornar_para()

##############################################################################################################

def exibir_opcoes_principal():
    '''
    Essa função exibe a página inicial do projeto com opções disponíveis.
    '''

    exibicao_personalizada('Bem-vindo',
                      f'{'1. Entrar':<30}\t3. Integrantes\n'
                      f'{'2. Cadastrar':<30}\t4. Sair')

    opcao_escolhida = forca_opcao('\nEscolha uma opção: ', range(1, 5))

    match opcao_escolhida:
        case 1: pagina_login()
        case 2: pagina_cadastro()
        case 3: pagina_readme()
        case 4: finalizar_app()

def exibir_readme(caminho_arquivo='README.md'):
    '''
    Exibe o conteúdo de um arquivo de texto. O README é usado como padrão.
    Recebe o caminho do arquivo como parâmetro.
    '''

    if not os.path.exists(caminho_arquivo):
        criar_readme(caminho_arquivo)
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.readlines()
            integrantes = []

            for linha in conteudo:
                if 'RM' in linha:
                    integrantes.append(linha.strip())

            exibicao_personalizada('Integrantes')
            print('', *integrantes, sep='\n', end='\n\n')

    except IOError as e:
        print(f'Erro ao ler o arquivo {caminho_arquivo}: {e}')
    finally:
        input('Pressione ENTER para continuar')

def criar_readme(caminho_arquivo):
    '''
    Cria um arquivo README com um conteúdo padrão se ele não existir.
    Recebe o caminho do arquivo como parâmetro.
    '''

    conteudo_padrao = ('''
# Computational Thinking with Python

## Integrantes

- Erik Yuuta Goto - RM558076
- Gabriel Guerreiro Escobosa Vallejo - RM554973
- Guilherme Vieira Augusto - RM557264
- Vinicius Vilas Boas - RM557843
- Wendell dos Santos Silva - RM558859

## Descrição

Rede social focada em interação entre o público da Formula E com sistema de comunidade, quizzes e recompensas.

## Instruções de uso

Navegação feita apenas com números.

## Requisitos

Bibliotecas padrões do python

## Dependências

Dependências básicas do python

## Informações relevantes

Cada perfil contém suas próprias informações independentes, possibilitando cada usuário ter seus pontos, recordes, equipe favorita e login.
''')

    try:
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo_padrao)
            print(f'O arquivo {caminho_arquivo} foi criado com conteúdo padrão.')
    except IOError as e:
        print(f'Erro ao criar o arquivo {caminho_arquivo}: {e}')

##############################################################################################################

def exibir_opcoes_menu():
    '''
    Essa função exibe a página principal do projeto com opções disponíveis.
    '''

    exibicao_personalizada('Menu',
                      f'{'1. Comunidade':<30}\t5. Próxima corrida\n'
                      f'{'2. Quiz Diário':<30}\t6. Recompensas\n'
                      f'{'3. Ranking':<30}\t7. Meu perfil\n'
                      f'{'4. Equipes':<30}\t8. Sair')

    opcao_escolhida = forca_opcao('\nEscolha uma opção: ', range(1, 9))

    match opcao_escolhida:
        case 1: menu()
        case 2: menu()
        case 3: menu()
        case 4: pagina_equipes()
        case 5: pagina_corrida()
        case 6: menu()
        case 7: pagina_perfil()
        case 8: main()

def exibir_opcoes_equipes():
    texto = ''
    for i in range(len(lista_equipes) - 2):
        if i % 2 == 0:
            texto += f'{lista_equipes[i]:<30}\t{lista_equipes[i + 1]}\n'
    texto += f'{lista_equipes[-2]}'

    exibicao_personalizada('Equipes', texto)

    print(f'Sua equipe favorita: {usuario['equipe_favorita']}\n\n'
          f'{'1. Alterar equipe favorita':<30}\t2. Voltar\n'
          f'{'=' * 60}')

    opcao_escolhida = forca_opcao('\nEscolha uma opção: ', range(1, 3))

    match opcao_escolhida:
        case 1: alterar_equipe(pagina_equipes)
        case 2: menu()

def exibir_corrida():
    evento = proxima_corrida()

    if evento is not None:
        exibicao_personalizada('Próxima Corrida',
                               f'{'Data:':<30}\t{evento['data']}\n'
                               f'{'Cidade:':<30}\t{evento['cidade']}\n'
                               f'{'País:':<30}\t{evento['pais']}\n'
                               f'{'Round:':<30}\t{evento['round']}')
    else:
        print('Não há corridas próximas')

    input('\nPressione ENTER para continuar')

def exibir_opcoes_perfil():
    '''
    Exibe o perfil do usuário de forma organizada.
    '''

    exibicao_personalizada('Perfil',
                      f'Nome: {usuario['nome']}\n'
                      f'Equipe Favorita: {usuario['equipe_favorita']}\n'
                      f'Pontuação Atual: {usuario['pontuacao_atual']}\n'
                      f'Jogou Hoje: {'Sim' if usuario['jogou_hoje'] else 'Não'}\n'
                      f'Sequência Atual: {usuario['sequencia_atual']}\n'
                      f'Melhor Sequência: {usuario['melhor_sequencia']}')

    print(f'{'1. Alterar nome':<30}\t3. Alterar equipe favorita\n'
          f'{'2. Alterar senha':<30}\t4. Voltar\n'
          f'{'=' * 60}')

    opcao_escolhida = forca_opcao('\nEscolha uma opção: ', range(1, 5))

    match opcao_escolhida:
        case 1: pagina_perfil()
        case 2: pagina_perfil()
        case 3: alterar_equipe(pagina_perfil)
        case 4: menu()

##############################################################################################################

def main():
    '''
    Função principal que inicia o programa.
    '''

    global usuario
    usuario = None

    titulo(True)
    exibir_opcoes_principal()

def pagina_cadastro():
    '''
    Função que exibe a página de cadastro.
    '''

    titulo()
    exibicao_personalizada('Cadastrar')
    cadastrar()
    main()

def pagina_login():
    '''
    Função que exibe a página de login.
    '''

    global usuario
    titulo()

    exibicao_personalizada('Entrar')
    id_usuario = entrar()
    if id_usuario is not None:
        usuario = lista_usuarios[id_usuario]
        menu()
    else:
        main()

def pagina_readme():
    '''
    Função que exibe a página do README.
    '''

    titulo()
    exibir_readme()
    main()

def menu():
    '''
    Função que exibe a página de menu.
    '''

    titulo()
    print(f'\nOlá {usuario['nome']}')
    exibir_opcoes_menu()

def pagina_equipes():
    '''
    Função que exibe a página de equipes.
    '''

    titulo()
    exibir_opcoes_equipes()

def pagina_corrida():
    '''
    Função que exibe a página de corridas.
    '''

    titulo()
    exibir_corrida()
    menu()

def pagina_perfil():
    '''
    Função que exibe a página de perfil.
    '''

    titulo()
    exibir_opcoes_perfil()

##############################################################################################################

if __name__ == '__main__':
    main()
