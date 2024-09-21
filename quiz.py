import random
from app import *

lista_quiz = [
    {
        'pergunta': "Em que ano foi realizada a primeira temporada da Fórmula E?",
        'alternativas': ["1. 2012-2013", "2. 2013-2014", "3. 2014-2015", "4. 2015-2016"],
        'resposta': 3
     },
    {
        'pergunta': "Quem foi o primeiro campeão da Fórmula E?",
        'alternativas': ["1. Sebastien Buemi", "2. Lucas di Grassi", "3. Nelson Piquet Jr.", "4. Jean-Éric Vergne"],
        'resposta': 3
    },
    {
        'pergunta': "Qual é o nome do carro usado na segunda geração da Fórmula E?",
        'alternativas': ["1. Gen1", "2. eCar", "3. Electrico", "4. Gen2"],
        'resposta': 4
    },
    {
        'pergunta': "Quantas equipes competem atualmente na Fórmula E?",
        'alternativas': ["1. 9 equipes", "2. 10 equipes", "3. 11 equipes", "4. 12 equipes"],
        'resposta': 3
    },
    {
        'pergunta': "Qual é o principal fornecedor de pneus da Fórmula E?",
        'alternativas': ["1. Pirelli", "2. Bridgestone", "3. Goodyear", "4. Michelin"],
        'resposta': 4
    },
    {
        'pergunta': "Quem é o piloto com mais vitórias na história da Fórmula E?",
        'alternativas': ["1. Lucas di Grassi", "2. Sebastien Buemi", "3. Jean-Éric Vergne", "4. Nelson Piquet Jr."],
        'resposta': 2
    },
    {
        'pergunta': "Em que cidade foi realizada a primeira corrida de Fórmula E?",
        'alternativas': ["1. Nova York, EUA", "2. Paris, França", "3. Londres, Reino Unido", "4. Pequim, China"],
        'resposta': 4
    },
    {
        'pergunta': "Qual equipe venceu o campeonato de equipes na temporada 2019-2020?",
        'alternativas': ["1. Venturi Racing", "2. Mahindra Racing", "3. Envision Virgin Racing", "4. DS Techeetah"],
        'resposta': 4
    },
    {
        'pergunta': "Qual é o nome do sistema que os pilotos ativam para ganhar potência extra passando por uma zona específica na pista?",
        'alternativas': ["1. Modo de Potência (Power Mode)", "2. Modo Turbo (Turbo Mode)", "3. Modo de Energia (Energy Mode)", "4. Modo Ataque (Attack Mode)"],
        'resposta': 4
    },
    {
        'pergunta': "Qual cidade sediou a primeira corrida noturna da Fórmula E?",
        'alternativas': ["1. Cingapura", "2. Nova York", "3. Riad", "4. Roma"],
        'resposta': 3
    },
    {
        'pergunta': "Qual é o nome do sistema de recuperação de energia usado na Fórmula E?",
        'alternativas': ["1. KERS", "2. ERS", "3. DRS", "4. FOM"],
        'resposta': 2
    },
    {
        'pergunta': "Quem foi o primeiro piloto a vencer uma corrida de Fórmula E?",
        'alternativas': ["1. Nelson Piquet Jr.", "2. Lucas di Grassi", "3. Sebastien Buemi", "4. Jean-Éric Vergne"],
        'resposta': 1
    },
    {
        'pergunta': "Qual é a principal característica dos circuitos da Fórmula E?",
        'alternativas': ["1. Circuitos de alta velocidade", "2. Circuitos urbanos", "3. Circuitos off-road", "4. Circuitos mistos"],
        'resposta': 2
    },
    {
        'pergunta': "Qual é o nome do evento que ocorre no final de cada temporada da Fórmula E?",
        'alternativas': ["1. E-Prix", "2. E-Playoff", "3. E-Championship", "4. E-Final"],
        'resposta': 1
    }
]

def sorteia_pergunta():
    indice = random.randint(0, len(lista_quiz) - 1)
    quiz_do_dia = lista_quiz[indice]
    pergunta = quiz_do_dia['pergunta']
    exibicao_personalizada('Quiz diário', pergunta)
    print(*quiz_do_dia['alternativas'], sep='\n')
    print(f'{'=' * 60}')
    resposta = forca_opcao('\nDigite uma opção: ', range(1, 5))
    if resposta == quiz_do_dia['resposta']:
        return True
    return False