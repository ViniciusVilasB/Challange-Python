import unittest
from time import localtime

from ..main import atualiza_comunidade, feed, fazer_postagem

class TestPostagens(unittest.TestCase):

    def test_atualiza_comunidade(self):
        novo_post = ['', localtime().tm_yday, "Testando", 1, localtime().tm_hour, localtime().tm_min]
        atualiza_comunidade(novo_post)
        self.assertIn("Testando", feed[-1][0])

    def test_fazer_postagem(self):
        feed_len = len(feed)
        fazer_postagem()
        self.assertGreater(len(feed), feed_len)


if __name__ == '__main__':
    unittest.main()
