from unittest import TestCase

from ReadFunVar import ReadFunVar


class TestReadFunVar(TestCase):
    def setUp(self):
        with open('fun_test.tsv', 'w') as ft:
            ft.write('1 \t 2 \t 3\n')
            ft.write('4 \t 5 \t 6')
        with open('fun_test.tsv', 'w') as vt:
            vt.write('1 \t 2 \t 3\n')
            vt.write('4 \t 5 \t 6')
        self.rfv = ReadFunVar("fun_test.tsv", "var_test.tsv")

    def test_should_save_fun_value_return_fun_file_for_given_pair(self):
        self.rfv.save_fun_value('fun_test_res.txt', self.rfv.best_strike)
        with open('fun_test_res.txt', 'r') as fin:
            self.assertEqual('4 \t 5 \t 6', fin.readline())
