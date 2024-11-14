from src import file_with_funcs
from unittest import TestCase
from time import time

class SampleUnit(TestCase):

    def test_method1(self):
        pre = time()
        getted = file_with_funcs.get_time()

        assert getted >= pre
