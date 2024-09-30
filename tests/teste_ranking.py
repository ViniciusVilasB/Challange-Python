import unittest

from ..ranking import define_top_10

class TestRanking(unittest.TestCase):

    def test_define_top_10(self):
        top10 = define_top_10()
        self.assertEqual(len(top10), 10)


if __name__ == '__main__':
    unittest.main()
