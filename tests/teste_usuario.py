import unittest

from ..usuarios import lista_usuarios
from ..cadastro import cadastrar, alterar_nome, alterar_senha

class TestUsuario(unittest.TestCase):

    def test_alterar_nome(self):
        usuario = {'nome': 'João'}
        novo_nome = alterar_nome('João')
        self.assertNotEqual(usuario['nome'], novo_nome)

    def test_alterar_senha(self):
        usuario = {'senha': '1234'}
        nova_senha = alterar_senha('1234')
        self.assertNotEqual(usuario['senha'], nova_senha)

    def test_cadastro(self):
        initial_count = len(lista_usuarios)
        cadastrar('NovoUsuario', 'senha')
        self.assertEqual(len(lista_usuarios), initial_count + 1)


if __name__ == '__main__':
    unittest.main()
