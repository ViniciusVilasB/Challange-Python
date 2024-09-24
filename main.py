##############################################################################################################

from time import localtime

from usuarios import lista_usuarios
from cadastro import cadastrar, alterar_nome, alterar_senha
from login import entrar
from ranking import define_top_10

from services import *

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

feed = [['Nenhuma publicação ainda\n']]

##############################################################################################################

def alterar_equipe(retornar_para):
    texto = listar_equipes(True)
    exibicao_personalizada('Altere a equipe', texto)

    print(f'Favorita atual: {usuario['equipe_favorita']}')
    opcao_escolhida = forca_opcao('\nEscolha uma nova equipe para acompanhar: ', range(1, 13))

    usuario['equipe_favorita'] = lista_equipes[opcao_escolhida - 1]['nome']

    return retornar_para()

def exibir_detalhes():
    if usuario['equipe_favorita'] != 'Nenhuma':
        for equipe in lista_equipes:
            if equipe['nome'] == usuario['equipe_favorita']:
                exibicao_personalizada(usuario['equipe_favorita'],
                                       f'{'Nome:':<30}\t{equipe['nome']}\n'
                                       f'{'Vitórias:':<30}\t{equipe['vitorias']}\n'
                                       f'{'Pódios:':<30}\t{equipe['podios']}\n'
                                       f'{'Corridas:':<30}\t{equipe['corridas']}')
                break
    else:
        print('Você não possui uma equipe favorita.')
    input('Pressione ENTER para continuar')
    pagina_equipes()

def muda_nome():
    exibicao_personalizada('Altere seu nome')
    usuario['nome'] = alterar_nome(usuario['nome'])
    pagina_perfil()

def muda_senha():
    exibicao_personalizada('Altere sua senha')
    usuario['senha'] = alterar_senha(usuario['senha'])
    pagina_perfil()

def atualiza_comunidade(novo_post=''):
    global feed

    if novo_post:
        feed.append(novo_post)
        if feed[0][0] == 'Nenhuma publicação ainda\n':
            feed.pop(0)

    if feed[0][0] != 'Nenhuma publicação ainda\n':
        for i in range(len(feed)):
            dia_do_post = feed[i][1]
            dias_passados = localtime().tm_yday - dia_do_post
            hora_do_post = feed[i][4]
            min_do_post = feed[i][5]

            if dias_passados == 0:
                if localtime().tm_hour == hora_do_post and localtime().tm_min == min_do_post:
                    horario = f'{localtime().tm_hour}:{localtime().tm_min}'
                else:
                    horario = f'{hora_do_post}:{min_do_post}'
            elif dias_passados < 7:
                horario = f'{dias_passados} dia(s) atrás'
            else:
                semanas = dias_passados // 7
                horario = f'{semanas} semana(s) atrás'

            id_autor = feed[i][3]
            nome_autor = lista_usuarios[id_autor]['nome']
            equipe_autor = lista_usuarios[id_autor]['equipe_favorita']

            post = feed[i][2]

            feed[i][0] = f'{horario}: @{nome_autor}({equipe_autor}): {post}\n'

def fazer_postagem():
    post = input('Digite sua postagem: ')

    novo_post = ['', localtime().tm_yday, post, usuario['id'], localtime().tm_hour, localtime().tm_min]
    atualiza_comunidade(novo_post)

def itens_disponiveis(itens):
    itens_filtrados = 0

    msg = ''
    for item in itens:
        if item['pontos'] < usuario['pontuacao_atual']:
            itens_filtrados += 1
            msg += f'{itens_filtrados}. {item['item']} - {item['pontos']} pontos\n'
    msg += f'\nVocê possui {usuario['pontuacao_atual']} pontos'

    if itens_filtrados == 0:
        print('Você não possui pontos o suficiente para comprar um item')
        input('Digite ENTER para continuar')
    else:
        exibicao_personalizada('Itens disponíveis', msg)
        opcao_escolhida = forca_opcao(f'Escolha um item para comprar (0 para voltar): ', range(itens_filtrados + 1))

        match opcao_escolhida:
            case 0: pass
            case _:
                usuario['pontuacao_atual'] -= itens[opcao_escolhida - 1]['pontos']
                print(f'\n{itens[opcao_escolhida - 1]['item']} comprado por {itens[opcao_escolhida - 1]['pontos']} pontos.')
                input('Pressione ENTER para continuar')

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

def exibir_readme(caminho_arquivo='./README.md'):
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
        input(f'{'=' * 50}\n'
              'Pressione ENTER para continuar')

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

    print(f'\nOlá, {usuario['nome']}!')
    opcao_escolhida = forca_opcao('Escolha uma opção: ', range(1, 9))

    atualiza_comunidade()

    match opcao_escolhida:
        case 1: pagina_comunidade()
        case 2: pagina_quiz()
        case 3: pagina_ranking()
        case 4: pagina_equipes()
        case 5: pagina_corrida()
        case 6: pagina_recompensas()
        case 7: pagina_perfil()
        case 8: main()

    menu()

def exibir_opcoes_comunidade():
    global feed

    atualiza_comunidade()

    exibir = ''
    for i in range(len(feed)):
        exibir += f'{feed[i][0]}'

    exibicao_personalizada('Comunidade', '\n' + exibir)
    print(f'{'1. Fazer publicação':<30}\t2. Voltar\n'
          f'{'=' * 60}')

    opcao_escolhida = forca_opcao('\nEscolha uma opção: ', range(1, 3))

    match opcao_escolhida:
        case 1: fazer_postagem(); exibir_opcoes_comunidade()
        case 2: pass

def exibir_opcoes_quiz():
    if not usuario['jogou_hoje']:
        acertou, resposta_certa = sorteia_pergunta()
        if acertou:
            usuario['sequencia_atual'] += 1
            usuario['pontuacao_atual'] += 100
            print(f'Resposta correta! Sequência atual é de: {usuario['sequencia_atual']}')
        else:
            usuario['sequencia_atual'] = 0
            print(f'Resposta errada. A resposta certa era a número {resposta_certa}')

        if usuario['sequencia_atual'] > usuario['melhor_sequencia']:
            usuario['melhor_sequencia'] = usuario['sequencia_atual']

        usuario['jogou_hoje'] = True
    else:
        print('Você já jogou hoje')
    input('\nPressione ENTER para continuar')

def exibir_opcoes_equipes():
    texto = listar_equipes()
    exibicao_personalizada('Equipes', texto)

    print(f'Sua equipe favorita: {usuario['equipe_favorita']}\n\n'
          f'{'1. Alterar equipe favorita':<30}\t3. Voltar\n'
          f'2. Detalhes sobre favorita\n'
          f'{'=' * 60}')

    opcao_escolhida = forca_opcao('\nEscolha uma opção: ', range(1, 4))

    match opcao_escolhida:
        case 1: alterar_equipe(exibir_opcoes_equipes)
        case 2: exibir_detalhes()
        case 3: pass

def exibir_ranking():
    lista_top10 = define_top_10()
    msg = ''

    for i in range(len(lista_top10)):
        msg += f'{i + 1}. {lista_top10[i]['nome']}: {lista_top10[i]['melhor_sequencia']} acertos em sequência'
        if i != len(lista_top10) - 1:
            msg += '\n'

    exibicao_personalizada('Ranking', msg)
    input('Pressione ENTER para continuar')

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

def exibir_opcoes_recompensas():
    itens = [
        {'item' : 'Copo personalizado' , 'pontos' : 2000},
        {'item' : 'Boné', 'pontos' : 5000},
        {'item' : 'Camiseta', 'pontos' : 8000},
        {'item' : 'Ingresso', 'pontos' : 20000},
        {'item' : '2 ingressos', 'pontos' : 30000},
    ]

    msg = ''
    for item in itens:
        msg += f'- {item['item']} - {item['pontos']} pontos\n'
    msg += f'\nVocê possui {usuario['pontuacao_atual']} pontos'

    exibicao_personalizada('Recompensas', msg)
    print(f'{'1. Comprar item':<30}\t2. Voltar\n'
          f'{'=' * 60}')

    opcao_escolhida = forca_opcao('Escolha uma opção: ', range(1, 3))

    match opcao_escolhida:
        case 1: itens_disponiveis(itens)
        case 2: menu()
    pagina_recompensas()

def exibir_opcoes_perfil():
    '''
    Exibe o perfil do usuário de forma organizada.
    '''

    exibicao_personalizada('Perfil',
                      f'Nome: {usuario['nome']}\n'
                      f'Equipe Favorita: {usuario['equipe_favorita']} (Vá para a aba "Equipes" para mais)\n'
                      f'Pontuação Atual: {usuario['pontuacao_atual']}\n'
                      f'Jogou Hoje: {'Sim' if usuario['jogou_hoje'] else 'Não'}\n'
                      f'Sequência Atual: {usuario['sequencia_atual']}\n'
                      f'Melhor Sequência: {usuario['melhor_sequencia']}')

    print(f'{'1. Alterar nome':<30}\t3. Alterar equipe favorita\n'
          f'{'2. Alterar senha':<30}\t4. Voltar\n'
          f'{'=' * 60}')

    opcao_escolhida = forca_opcao('\nEscolha uma opção: ', range(1, 5))

    match opcao_escolhida:
        case 1: muda_nome()
        case 2: muda_senha()
        case 3: alterar_equipe(pagina_perfil)
        case 4: pass

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
    exibir_opcoes_menu()

def pagina_comunidade():
    '''
    Função que exibe a página de comunidade.
    '''

    titulo()
    exibir_opcoes_comunidade()

def pagina_quiz():
    '''
    Função que exibe a página de quiz diário.
    '''

    titulo()
    exibir_opcoes_quiz()

def pagina_equipes():
    '''
    Função que exibe a página de equipes.
    '''

    titulo()
    exibir_opcoes_equipes()

def pagina_ranking():
    '''
    Função que exibe a página de ranking.
    '''

    titulo()
    exibir_ranking()

def pagina_corrida():
    '''
    Função que exibe a página de corridas.
    '''

    titulo()
    exibir_corrida()

def pagina_recompensas():
    '''
    Função que exibe a página de recompensas.
    '''

    titulo()
    exibir_opcoes_recompensas()

def pagina_perfil():
    '''
    Função que exibe a página de perfil.
    '''

    titulo()
    exibir_opcoes_perfil()

##############################################################################################################

if __name__ == '__main__':
    main()
