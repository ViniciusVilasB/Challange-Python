from datetime import datetime
import locale
import os

lista_proximas_corridas = [
    {'data': '7 de dezembro de 2024', 'cidade': 'São Paulo', 'pais': 'Brasil', 'round': 1},
    {'data': '11 de janeiro de 2025', 'cidade': 'Cidade do México', 'pais': 'México', 'round': 2},
    {'data': '14 de fevereiro de 2025', 'cidade': 'Jidá', 'pais': 'Arábia Saudita', 'round': 3},
    {'data': '15 de fevereiro de 2025', 'cidade': 'Jidá', 'pais': 'Arábia Saudita', 'round': 4},
    {'data': '8 de março de 2025', 'cidade': 'Não definido', 'pais': 'Não definido', 'round': 5},
    {'data': '12 de abril de 2025', 'cidade': 'Miami', 'pais': 'Estados Unidos', 'round': 6},
    {'data': '3 de maio de 2025', 'cidade': 'Mônaco', 'pais': 'Mônaco', 'round': 7},
    {'data': '4 de maio de 2025', 'cidade': 'Mônaco', 'pais': 'Mônaco', 'round': 8},
    {'data': '17 de maio de 2025', 'cidade': 'Tóquio', 'pais': 'Japão', 'round': 9},
    {'data': '18 de maio de 2025', 'cidade': 'Tóquio', 'pais': 'Japão', 'round': 10}
]

def encontrar_proxima_corrida(lista_corridas):
    '''
    Encontra a próxima corrida na lista de corridas.
    '''

    data_atual = datetime.now()
    proxima_corrida = None

    for corrida in lista_corridas:
        data_corrida = datetime.strptime(corrida['data'], '%d de %B de %Y')

        if data_corrida > data_atual:
            if proxima_corrida is None or data_corrida < datetime.strptime(proxima_corrida['data'], '%d de %B de %Y'):
                proxima_corrida = corrida

    return proxima_corrida

def proxima_corrida():
    if os.name == 'nt':
        locale.setlocale(locale.LC_TIME, 'portuguese')
    else:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

    if proxima_corrida:
        return encontrar_proxima_corrida(lista_proximas_corridas)
    else:
        return None
