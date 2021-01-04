import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_full_program_7(self):
        input = """
        Function: main
            Body:
            Var: x[5] = {1,2,3,4,5};
            EndBody."""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,555))