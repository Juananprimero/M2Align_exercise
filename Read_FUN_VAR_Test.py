from unittest import TestCase
from ReadFunVar import ReadFunVar

class TestReadFunVar(TestCase):
    def setUp(self):
        self.read = ReadFunVar("FUN.BB11001.tsv", "VAR.BB11001.tsv")


    def test_should_save_fun_value_return_fun_file_for_given_pair(self):
        pass

    def test_should_save_var_value_return_var_file_for_given_pair(self):
        pass

    def test_should_throw_exception_if_the_file_doesnt_exist(self):
            pass

    def test_should_throw_ValueError_if_the_format_of_FUN_File_is_not_correct(self):
        #for example there is ' ' instead of '\t'
        pass



