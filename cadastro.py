from usuarios import usuario_base, lista_usuarios

def criar_nome():
    while True:
        nome = input('\nDigite o seu nome: ')

        while not nome:
            nome = input('Nome não pode ser vazio: ')

        for usuario in lista_usuarios:
            if usuario['nome'] == nome:
                print('Já existe um usuário com esse nome\n')
                break
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
