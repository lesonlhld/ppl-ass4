import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_array_26(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[2][2] = {{1,2},{3,4}};
                        x[0][1] = 5;
                        print(string_of_int(x[0][1]));
                    EndBody."""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,555))
