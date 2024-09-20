from usuarios import *

def verifica_nome(nome):
    for usuario in lista_usuarios:
        if usuario['nome'] == nome:
            return True
    return False

def criar_nome():
    while True:
        nome = input('\nDigite o seu nome: ')

        while not nome:
            nome = input('Nome não pode ser vazio: ')

        if verifica_nome(nome):
            print('Já existe um usuário com esse nome\n')
        else:
            return nome

def criar_senha(nome):
    while True:
        senha = input(f'Digite a senha para o usuario "{nome}": ')

        while not senha:
            senha = input(f'Senha não pode ser vazia: ')

        confirmar_senha = input('Confirme sua senha: ')

        if confirmar_senha != senha:
            print('\nAs senhas não coincidem')
        else:
            return senha

def cadastrar():
    nome = criar_nome()
    senha = criar_senha(nome)

    novo_usuario = usuario_base.copy()
    novo_usuario['nome'] = nome
    novo_usuario['senha'] = senha

    lista_usuarios.append(novo_usuario)

    id_novo_usuario = len(lista_usuarios) - 1
    lista_usuarios[id_novo_usuario]['id'] = id_novo_usuario

    print(f'Usuário "{nome}" criado com sucesso!\n')

def alterar_nome(nome):
    while True:
        novo_nome = input('\nDigite seu novo nome: ')

        while not novo_nome:
            novo_nome = input('Nome não pode ser vazio: ')

        while novo_nome == nome:
            novo_nome = input('Novo nome não pode ser igual ao anterior: ')

        if verifica_nome(novo_nome):
            print('Este nome ja está sendo usado')
        else:
            print(f'Nome alterado para {novo_nome}')
            return novo_nome

def alterar_senha(senha):
    confirmar_senha = input('Digite a senha atual: ')

    while confirmar_senha != senha:
        print('Senhas não coincidem')
        confirmar_senha = input('Digite a senha atual: ')

    while True:
        nova_senha = input('\nDigite a nova senha: ')

        while not nova_senha:
            nova_senha = input('Senha não pode ser vazia: ')

        confirmar_nova_senha = input('Confirme sua senha: ')

        if nova_senha != confirmar_nova_senha:
            print('\nAs senhas não coincidem')
        else:
            print('Senha alterada')
            return nova_senha