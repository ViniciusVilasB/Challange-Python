from usuarios import lista_usuarios

def verifica_usuario(nome, senha):
    for usuario in lista_usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            return usuario['id']
    return None

def entrar():
    nome = input('\nDigite o seu nome: ')
    senha = input('Digite a sua senha: ')

    id_usuario = verifica_usuario(nome, senha)
    if id_usuario is not None:
        return id_usuario
    else:
        print('\nNome ou senha estão incorretos')
        input('Presione ENTER para continuar')
        return None
