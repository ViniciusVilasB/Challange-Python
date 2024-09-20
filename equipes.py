lista_equipes = [
    {'nome': 'ABT Cupra', 'vitorias': 14, 'podios': 47, 'corridas': 115},
    {'nome': 'Andretti', 'vitorias': 11, 'podios': 37, 'corridas': 132},
    {'nome': 'DS Penske', 'vitorias': 3, 'podios': 17, 'corridas': 132},
    {'nome': 'Envision', 'vitorias': 16, 'podios': 53, 'corridas': 132},
    {'nome': 'ERT', 'vitorias': 2, 'podios': 6, 'corridas': 132},
    {'nome': 'Jaguar TCS', 'vitorias': 16, 'podios': 46, 'corridas': 111},
    {'nome': 'Mahindra', 'vitorias': 5, 'podios': 24, 'corridas': 131},
    {'nome': 'Maseratti MSG', 'vitorias': 10, 'podios': 27, 'corridas': 132},
    {'nome': 'Mclaren', 'vitorias': 8, 'podios': 26, 'corridas': 87},
    {'nome': 'Nissan', 'vitorias': 19, 'podios': 47, 'corridas': 132},
    {'nome': 'Tag Heuer Porsche', 'vitorias': 12, 'podios': 22, 'corridas': 74},
    {'nome': 'Nenhuma'}
]

def listar_equipes(editar=False):
    texto = ''
    if editar:
        for i in range(len(lista_equipes) - 1):
            if i % 2 == 0:
                equipe_atual = lista_equipes[i]['nome']
                equipe_proxima = lista_equipes[i + 1]['nome']
                if lista_equipes[i] != lista_equipes[-2]:
                    texto += f'{i + 1}. {equipe_atual:<30}\t{i + 2}. {equipe_proxima}\n'
                else:
                    texto += f'{i + 1}. {equipe_atual:<30}\t{i + 2}. {equipe_proxima}'
    else:
        for i in range(len(lista_equipes) - 2):
            if i % 2 == 0:
                equipe_atual = lista_equipes[i]['nome']
                equipe_proxima = lista_equipes[i + 1]['nome']
                texto += f'{equipe_atual:<30}\t{equipe_proxima}\n'
        texto += f'{lista_equipes[-2]['nome']}'

    return texto
