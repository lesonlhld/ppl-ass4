import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        """Created automatically"""
        input = r"""Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_502(self):
        """Created automatically"""
        input = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,502))
        