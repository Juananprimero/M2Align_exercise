from unittest import TestCase

from read_fun_var import ReadFunVar


class TestReadFunVar(TestCase):
    def setUp(self):
        self.rfv = ReadFunVar("fun_test.tsv", "var_test.tsv")

    def test_should_save_fun_value_return_fun_file_for_given_pair(self):
        self.rfv.save_fun_value('fun_test_res.txt', self.rfv.best_strike)
        with open('fun_test_res.txt', 'r') as fin:
            self.assertEqual('2.937049554579437\t3.6036036036036037\t77.7027027027027', fin.readline().strip())

    def test_should_save_var_value_return_fun_file_for_given_pair(self):
        self.rfv.save_var_value('var_test_res.txt', self.rfv.best_strike)
        expected_result = \
            '>1aab_\n\
---GKGD---PKKPRG-KMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKE---KGKFEDMAKADKARYEREMKTY-----------IP-------PKGE\n\
>1j46_A\n\
------MQDRVKRP----MNAFIVWSRDQRRKMALENPRM--RNSEISKQLGYQWKMLT--EAEKW-PFFQEAQKLQAMHREKYPNY---KY-R---PRRK--AKMLPK--\n\
>1k99_A\n\
MKK---LKKHPDFPKKP-LTPYFRFFMEKRAKYAKLHPEM--SNLDLTKILSKKYKELP--EKKKM-KYIQDFQREKQEFERNLARF----REDHPDLI---QN--AKK--\n\
>2lef_A\n\
--------MHIKKP----LNAFMLYMKEMRANVVAE-STL-KESAAINQILGRRWHALSREEQA--K-YYELARKERQLHMQLYPGWSAR-D---NYGKKKKRKRE--K--\n'
        with open('var_test_res.txt', 'r') as fin:
            self.assertEqual(expected_result, ''.join(map(str, fin.readlines())))

