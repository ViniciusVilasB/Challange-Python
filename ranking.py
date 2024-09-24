from usuarios import lista_usuarios

def define_top_10():
    lista_sequencia = [usuario['melhor_sequencia'] for usuario in lista_usuarios]
    top_10 = []

    if len(lista_sequencia) < 10:
        sequencia_minima = min(lista_sequencia)
    else:
        sequencia_minima = sorted(lista_sequencia)[-10]

    for usuario in lista_usuarios:
        if usuario['melhor_sequencia'] >= sequencia_minima:
            posicao_final = len(top_10)

            for i in range(len(top_10)):
                if usuario['melhor_sequencia'] > top_10[i]['melhor_sequencia']:
                    posicao_final = i
                    break

            top_10.insert(posicao_final,
                          {'nome': usuario['nome'], 'melhor_sequencia': usuario['melhor_sequencia']})

            if len(top_10) > 10:
                top_10.pop()

    return top_10