import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # Variable Decleration
    def test_601(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 0;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,601))

    def test_606(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 0x123ABC;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,606))

    def test_607(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 0o1234;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,607))

    def test_602(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 1.234;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,602))

    def test_603(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 32.4e-1;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,603))

    def test_608(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = 12000.;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,608))

    def test_604(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = True;
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,604))

    def test_605(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "Chung Xon";
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,605))

    def test_609(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x = "\tHello moi nguoi @@ \n";
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,609))

    def test_610(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x[3] = {1,2,3};
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,610))

    def test_611(self):
        """Created automatically"""
        input = r"""Function: main
                   Body:
                   Var: x[3] = {1.2,2.3,3.4};
                   EndBody."""
        expect = r""""""
        self.assertTrue(TestCodeGen.test(input,expect,611))